"""Isolated installer fixtures: no printer paths or hardware are touched."""
import hashlib
import importlib.machinery
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
loader = importlib.machinery.SourceFileLoader('helix_installer', str(HERE / 'helixscreen-turkish-install'))
spec = importlib.util.spec_from_loader(loader.name, loader)
installer = importlib.util.module_from_spec(spec)
loader.exec_module(installer)


def digest(data):
    return hashlib.sha256(data).hexdigest()


class InstallerTests(unittest.TestCase):
    def setUp(self):
        # Windows does not expose POSIX executable bits on extensionless files.
        # Model them in fixtures only; production retains the strict mode check.
        if os.name == 'nt':
            original_mode = installer.stat.S_IMODE
            mode_patch = patch.object(installer.stat, 'S_IMODE', side_effect=lambda mode: original_mode(mode) | 0o111)
            mode_patch.start()
            self.addCleanup(mode_patch.stop)
        self.temporary = tempfile.TemporaryDirectory(prefix='helix-tr-fixture-')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.base = self.root / 'app'
        self.target = self.base / installer.VERSION
        self.payload = self.root / 'payload'
        self.files = [
            ('ui_xml/translations/tr.xml', None, b'new turkish'),
            ('ui_xml/translations/translations.xml', b'old translations', b'new translations'),
            ('ui_xml/wizard_language_chooser.xml', b'old wizard', b'new wizard'),
            ('bin/helix-screen', b'old binary', b'new binary')]
        records = []
        for name, old, new in self.files:
            destination = self.target / name
            source = self.payload / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            source.parent.mkdir(parents=True, exist_ok=True)
            if old is not None:
                destination.write_bytes(old)
                destination.chmod(0o755 if name.startswith('bin/') else 0o644)
            source.write_bytes(new)
            records.append({'path': name, 'source_sha256': digest(old) if old else None,
                            'sha256': digest(new), 'mode': 0o644})
        (self.payload / 'manifest.json').write_text(json.dumps(
            {'schema': 1, 'version': '1.0.0', 'platform': 'snapmaker-u1',
             'source_archive_sha256': installer.ARCHIVE_SHA256, 'files': records}), encoding='utf-8')
        (self.target / 'settings.json').write_bytes(b'{"language":"fr","private":"preserve"}')
        (self.target / 'ui_xml/translations/fr.xml').write_bytes(b'original French')

    def install(self, target=None):
        return installer.install(target or self.target, self.payload, self.base)

    def snapshot(self):
        return {path.relative_to(self.target).as_posix(): path.read_bytes()
                for path in self.target.rglob('*') if path.is_file()}

    def test_fresh_and_idempotent_keep_settings_and_other_language(self):
        before = self.snapshot()
        self.assertEqual(self.install(), 4)
        after = self.snapshot()
        for name, _, new in self.files:
            self.assertEqual(after[name], new)
        self.assertEqual(after['settings.json'], before['settings.json'])
        self.assertEqual(after['ui_xml/translations/fr.xml'], before['ui_xml/translations/fr.xml'])
        self.assertEqual(self.install(), 0)
        self.assertEqual(self.snapshot(), after)

    def test_staging_install(self):
        staging = self.base / 'tmp' / installer.VERSION
        staging.parent.mkdir()
        self.target.rename(staging)
        self.target = staging
        self.assertEqual(self.install(), 4)

    def test_unknown_binary_refused_without_changes(self):
        (self.target / 'bin/helix-screen').write_bytes(b'custom binary')
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, 'customized target'):
            self.install()
        self.assertEqual(self.snapshot(), before)

    def test_unknown_turkish_refused_without_changes(self):
        (self.target / 'ui_xml/translations/tr.xml').write_bytes(b'custom Turkish')
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, 'customized target'):
            self.install()
        self.assertEqual(self.snapshot(), before)

    def test_corrupt_payload_refused_without_changes(self):
        (self.payload / 'bin/helix-screen').write_bytes(b'corrupted')
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, 'checksum mismatch'):
            self.install()
        self.assertEqual(self.snapshot(), before)

    def test_unexpected_path_refused(self):
        with self.assertRaisesRegex(ValueError, 'Unexpected application directory'):
            self.install(self.root)

    def test_path_traversal_refused(self):
        document = json.loads((self.payload / 'manifest.json').read_text())
        document['files'][0]['path'] = '../escape'
        (self.payload / 'manifest.json').write_text(json.dumps(document))
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, 'Unexpected payload file list'):
            self.install()
        self.assertEqual(self.snapshot(), before)

    def test_copy_failure_leaves_originals_and_no_temporary_files(self):
        before = self.snapshot()
        real_stage = installer.stage
        calls = 0
        def fail_second(*args):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError('injected disk full')
            return real_stage(*args)
        with patch.object(installer, 'stage', side_effect=fail_second):
            with self.assertRaisesRegex(OSError, 'disk full'):
                self.install()
        self.assertEqual(self.snapshot(), before)

    def test_interrupted_commit_recovers_on_next_run(self):
        original_replace = installer.os.replace
        calls = 0
        def fail_second(*args):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError('injected power-loss boundary')
            return original_replace(*args)
        with patch.object(installer.os, 'replace', side_effect=fail_second):
            with self.assertRaisesRegex(OSError, 'power-loss boundary'):
                self.install()
        self.assertEqual((self.target / 'bin/helix-screen').read_bytes(), b'old binary')
        self.assertFalse(list(self.target.rglob('.quinry-tr-*')))
        self.assertEqual(self.install(), 3)
        self.assertEqual(self.install(), 0)

    def symlink(self, source, destination, directory=False):
        try:
            source.symlink_to(destination, target_is_directory=directory)
        except OSError as error:
            if os.name == 'nt' and directory:
                # NTFS directory junctions exercise real path-resolution checks
                # without requiring Windows' symbolic-link privilege.
                command = "New-Item -ItemType Junction -Path $args[0] -Target $args[1] | Out-Null"
                result = subprocess.run(['powershell.exe', '-NoProfile', '-Command',
                    '& { ' + command + ' }', str(source), str(destination)], capture_output=True)
                if result.returncode == 0:
                    return
            self.skipTest('Host symlinks unavailable: ' + str(error))

    def test_valid_latest_symlink(self):
        latest = self.base / 'latest'
        self.symlink(latest, self.target, True)
        self.assertEqual(self.install(latest), 4)

    def test_escaping_latest_symlink_refused(self):
        latest = self.base / 'latest'
        self.symlink(latest, self.root, True)
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, 'outside pinned version'):
            self.install(latest)
        self.assertEqual(self.snapshot(), before)

    def test_symlink_file_refused(self):
        destination = self.target / 'ui_xml/translations/tr.xml'
        self.symlink(destination, self.target / 'settings.json')
        with self.assertRaisesRegex(ValueError, 'Symlink target'):
            self.install()


if __name__ == '__main__':
    unittest.main(verbosity=2)
