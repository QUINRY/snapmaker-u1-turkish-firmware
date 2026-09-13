#!/usr/bin/env python3
"""Add Turkish as HelixScreen U1 v1.0.0's tenth locale; preserve nine locales."""
from __future__ import annotations
from pathlib import Path
from io import BytesIO
import argparse,hashlib,json,logging,struct,sys

HERE=Path(__file__).resolve().parent
for parent in (HERE,*HERE.parents):
    for name in ('.retools','.retools_angr'):
        if (parent/name).is_dir():sys.path.insert(0,str(parent/name))
from elftools.elf.elffile import ELFFile
from keystone import Ks,KS_ARCH_ARM64,KS_MODE_LITTLE_ENDIAN
from capstone import Cs,CS_ARCH_ARM64,CS_MODE_LITTLE_ENDIAN

SOURCE=HERE/'helixscreen/bin/helix-screen'
OUTPUT=HERE/'output/bin/helix-screen'
MANIFEST=HERE/'patch_manifest.json'
REPORT=HERE/'verification_report.json'
SOURCE_SHA='e570921f12b94174dc3cea8063ec44b2a645e32a6d133e482d5fab4da04c19ae'
SOURCE_SIZE=15155112
OLD_RELA=0x4010
OLD_TOTAL=26024
OLD_RELATIVE=25867
LANGUAGE_CODES=['en','de','fr','es','ru','pt','it','zh','ja','tr']
ORIGINAL_ARRAYS=[0xe478a8,0xe72ee0]
ORIGINAL_WELCOME=0xe72f28
ORIGINAL_OPTIONS=0xc111fe

def digest(data): return hashlib.sha256(data).hexdigest()
def align(n): return (n+4095)&~4095
def offset(elf,address):
    for s in elf.iter_segments():
        if s['p_type']=='PT_LOAD' and s['p_vaddr']<=address<s['p_vaddr']+s['p_filesz']:
            return int(s['p_offset'])+address-int(s['p_vaddr'])
    raise ValueError(hex(address))
def string(data,elf,address):
    p=offset(elf,address);return data[p:data.index(0,p)].decode('utf-8')
def records(elf):
    return [(int(r['r_offset']),int(r['r_info']),int(r['r_addend'])) for r in elf.get_section_by_name('.rela.dyn').iter_relocations()]
def relmap(elf): return {a:c for a,b,c in records(elf) if b&0xffffffff==1027}
def asm(line,address):
    b,_=Ks(KS_ARCH_ARM64,KS_MODE_LITTLE_ENDIAN).asm(line,address,as_bytes=True)
    assert len(b)==4,(line,address)
    return bytes(b)
def jsonwrite(path,obj):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def patch():
    source=SOURCE.read_bytes();elf=ELFFile(BytesIO(source))
    assert len(source)==SOURCE_SIZE and digest(source)==SOURCE_SHA
    assert elf['e_machine']=='EM_AARCH64' and elf['e_type']=='ET_DYN'
    original=records(elf);rel=relmap(elf)
    assert len(original)==OLD_TOTAL
    assert all(info&0xffffffff==1027 for _,info,_ in original[:OLD_RELATIVE])
    assert all(info&0xffffffff!=1027 for _,info,_ in original[OLD_RELATIVE:])
    code_ptrs=[rel[ORIGINAL_ARRAYS[0]+i*8] for i in range(9)]
    assert [string(source,elf,p) for p in code_ptrs]==LANGUAGE_CODES[:9]
    assert code_ptrs==[rel[ORIGINAL_ARRAYS[1]+i*8] for i in range(9)]
    welcome_ptrs=[rel[ORIGINAL_WELCOME+i*8] for i in range(9)]
    welcome_text=[string(source,elf,p) for p in welcome_ptrs]
    assert welcome_text==['Welcome!','Willkommen!','Bienvenue!','¡Bienvenido!','Добро пожаловать!','Bem-vindo!','Benvenuto!','欢迎！','ようこそ！']
    options=string(source,elf,ORIGINAL_OPTIONS)
    assert len(options.split('\n'))==9
    loads=[s for s in elf.iter_segments() if s['p_type']=='PT_LOAD']
    base=align(max(s['p_vaddr']+s['p_memsz'] for s in loads));fileoff=align(len(source))
    rela_size=(OLD_TOTAL+20)*24
    payload=bytearray(align(0x100+rela_size))
    def append(value):
        address=base+len(payload);payload.extend(value);return address
    array=append(b'\0'*80);welcome=append(b'\0'*80)
    trcode=append(b'tr\0');trwelcome=append('Hoş geldiniz!'.encode('utf-8')+b'\0')
    opt=append((options+'\nTürkçe').encode('utf-8')+b'\0')
    new=[]
    for target,values in [(array,code_ptrs+[trcode]),(welcome,welcome_ptrs+[trwelcome])]:
        for i,value in enumerate(values):
            slot=target+i*8
            struct.pack_into('<Q',payload,slot-base,value)
            new.append((slot,1027,value))
    all_rela=original[:OLD_RELATIVE]+new+original[OLD_RELATIVE:]
    payload[0x100:0x100+rela_size]=b''.join(struct.pack('<QQq',*r) for r in all_rela)
    signature=b'HELIXSCREEN-U1-v1.0.0-TR-ADDITIVE\0'
    payload[:len(signature)]=signature
    out=bytearray(source);changes=[]
    def write(p,b,reason,expected=None):
        before=bytes(out[p:p+len(b)])
        if expected is not None:assert before==expected,(hex(p),reason,before.hex(),expected.hex())
        out[p:p+len(b)]=b;changes.append({'offset':p,'size':len(b),'before':before.hex(),'after':b.hex(),'reason':reason})
    def ins(address,old,new,reason):
        write(offset(elf,address),asm(new,address),reason,asm(old,address))
    def pair(adrp,add,register,destination,old,new,reason):
        ins(adrp,f'adrp {register}, 0x{old&~4095:x}',f'adrp {register}, 0x{new&~4095:x}',reason+' page')
        ins(add,f'add {destination}, {register}, #{old&4095}',f'add {destination}, {register}, #{new&4095}',reason+' offset')
    pair(0x3bf654,0x3bf658,'x1','x1',ORIGINAL_ARRAYS[0],array,'settings index-to-code table')
    pair(0x3c0058,0x3c005c,'x21','x21',ORIGINAL_ARRAYS[0],array,'settings code-to-index table')
    pair(0x6700c0,0x6700c8,'x22','x0',ORIGINAL_ARRAYS[1],array,'wizard language code table')
    ins(0x6700f0,'add x22, x22, #0xee0',f'add x22, x22, #{array&4095}','wizard persistent language code table')
    pair(0x6700c4,0x6700cc,'x3','x3',ORIGINAL_WELCOME,welcome,'wizard welcome logging table')
    pair(0x664a54,0x664a58,'x1','x1',ORIGINAL_WELCOME,welcome,'wizard welcome cycle table')
    pair(0x590448,0x59044c,'x1','x1',ORIGINAL_OPTIONS,opt,'settings dropdown options first caller')
    pair(0x5eb0b8,0x5eb0bc,'x1','x1',ORIGINAL_OPTIONS,opt,'settings dropdown options second caller')
    ins(0x3bf62c,'cmp w0, #8','cmp w0, #9','settings index bound tenth locale')
    ins(0x3c0074,'cmp x19, #9','cmp x19, #10','settings search ten locales')
    ins(0x670064,'cmp w0, #8','cmp w0, #9','wizard index bound tenth locale')
    ins(0x664a3c,'mov w1, #9','mov w1, #10','welcome cycle divisor ten')
    ins(0x664a4c,'add w1, w1, w1, lsl #3','add w1, w1, w1, lsl #2','welcome quotient multiply five')
    ins(0x664a50,'sub w0, w0, w1','sub w0, w0, w1, lsl #1','welcome modulo ten remainder')
    notes=[(i,s) for i,s in enumerate(elf.iter_segments()) if s['p_type']=='PT_NOTE' and s['p_vaddr']==0xe2f57c]
    assert len(notes)==1
    noteindex=notes[0][0]
    write(elf['e_phoff']+noteindex*elf['e_phentsize'],struct.pack('<IIQQQQQQ',1,6,fileoff,base,base,len(payload),len(payload),4096),'append RW PT_LOAD in optional ABI/build-package PT_NOTE slot')
    dynamic=elf.get_section_by_name('.dynamic')
    values={7:base+0x100,8:rela_size,0x6ffffff9:OLD_RELATIVE+20}
    for pos in range(dynamic['sh_offset'],dynamic['sh_offset']+dynamic['sh_size'],16):
        tag,value=struct.unpack_from('<qQ',source,pos)
        if tag in values:write(pos+8,struct.pack('<Q',values[tag]),f'update dynamic tag {tag}')
    idx=elf.get_section_index('.rela.dyn');sh=elf['e_shoff']+idx*elf['e_shentsize']
    for delta,value in [(16,base+0x100),(24,fileoff+0x100),(32,rela_size)]:write(sh+delta,struct.pack('<Q',value),'update relocation section header')
    out.extend(b'\0'*(fileoff-len(out)));out.extend(payload)
    OUTPUT.parent.mkdir(parents=True,exist_ok=True);OUTPUT.write_bytes(out)
    manifest={'source_sha256':SOURCE_SHA,'output_sha256':digest(out),'source_size':len(source),'output_size':len(out),'addresses':{'array':array,'welcome':welcome,'trcode':trcode,'trwelcome':trwelcome,'options':opt,'segment':base,'segment_file_offset':fileoff},'original_relocations':OLD_TOTAL,'added_relocations':20,'changes':changes,'existing_locales':LANGUAGE_CODES[:9],'added_locale':'tr','locale_count':10,'welcome_text':welcome_text+['Hoş geldiniz!']}
    jsonwrite(MANIFEST,manifest)
    verify(source,bytes(out),manifest)
    print('OUTPUT',OUTPUT,digest(out),len(out))
    return manifest

def verify(source,out,m):
    assert digest(source)==SOURCE_SHA and digest(out)==m['output_sha256']
    se=ELFFile(BytesIO(source));oe=ELFFile(BytesIO(out));r=relmap(oe);a=m['addresses'];checks=[]
    def check(name,value):
        assert value,name
        checks.append({'name':name,'passed':True})
    rr=records(oe);sr=records(se)
    check('all original relocation prefix entries preserved',rr[:OLD_RELATIVE]==sr[:OLD_RELATIVE])
    check('all original nonrelative suffix entries preserved',rr[OLD_RELATIVE+20:]==sr[OLD_RELATIVE:])
    check('only twenty new relative relocations',len(rr)==OLD_TOTAL+20 and all(info&0xffffffff==1027 for _,info,_ in rr[:OLD_RELATIVE+20]))
    check('all ten language codes resolve',[string(out,oe,r[a['array']+i*8]) for i in range(10)]==LANGUAGE_CODES)
    check('all ten welcome strings resolve',[string(out,oe,r[a['welcome']+i*8]) for i in range(10)]==m['welcome_text'])
    check('ten settings display options',string(out,oe,a['options']).split('\n')==string(source,se,ORIGINAL_OPTIONS).split('\n')+['Türkçe'])
    for addr in ORIGINAL_ARRAYS+[ORIGINAL_WELCOME]:check(f'original nine-entry table {addr:x} unchanged',source[offset(se,addr):offset(se,addr)+72]==out[offset(oe,addr):offset(oe,addr)+72])
    allowed=bytearray(len(source))
    for c in m['changes']:
        allowed[c['offset']:c['offset']+c['size']]=b'\1'*c['size']
        check(f'exact documented patch {c["offset"]:x}',out[c['offset']:c['offset']+c['size']].hex()==c['after'])
    check('no unlisted in-place byte changes',all(x==y or allowed[i] for i,(x,y) in enumerate(zip(source,out))))
    loads=[s for s in oe.iter_segments() if s['p_type']=='PT_LOAD']
    spans=sorted((s['p_vaddr'],s['p_vaddr']+s['p_memsz']) for s in loads)
    check('three non-overlapping load segments',len(loads)==3 and all(x[1]<=y[0] for x,y in zip(spans,spans[1:])))
    fontprefix=struct.pack('<IHH',160,224,96)
    fontmaps=[];pos=0
    while True:
        pos=source.find(fontprefix,pos)
        if pos<0:break
        if source[pos-32:pos-24]==struct.pack('<IHH',32,95,1):fontmaps.append(pos)
        pos+=1
    check('23 native Latin text cmaps include all Turkish codepoints',len(fontmaps)==23 and all(160<=ord(c)<384 for c in 'çğıöşüÇĞİÖŞÜ'))
    runtime=runtime_verify(out,m)
    check('all native runtime language probes passed',runtime['passed'])
    jsonwrite(REPORT,{'passed':True,'source_sha256':SOURCE_SHA,'output_sha256':digest(out),'checks':checks,'font_cmap_addresses':[hex(x) for x in fontmaps],'runtime':runtime,'physical_device_test':False})
    print('VERIFY',len(checks),'checks pass')

def runtime_verify(out,m):
    import angr,claripy
    for name in ('cle.loader','angr.calling_conventions','angr.storage.memory_mixins.default_filler_mixin'):logging.getLogger(name).setLevel(logging.ERROR)
    b=0x40000000;a=m['addresses'];project=angr.Project(BytesIO(out),auto_load_libs=False,main_opts={'base_addr':b})
    opts={angr.options.ZERO_FILL_UNCONSTRAINED_REGISTERS,angr.options.ZERO_FILL_UNCONSTRAINED_MEMORY}
    def cstr(state,p):return state.mem[state.solver.eval(p)].string.concrete.decode('utf-8')
    def cpp(state,p):return cstr(state,state.memory.load(state.solver.eval(p),8,endness='Iend_LE'))
    def writecpp(state,p,text):
        raw=text.encode()+b'\0';state.memory.store(p,struct.pack('<QQ',p+16,len(raw)-1));state.memory.store(p+16,raw)
    class Ctor(angr.SimProcedure):
        def run(self,obj,chars):writecpp(self.state,self.state.solver.eval(obj),cstr(self.state,chars));return obj
    class Equal(angr.SimProcedure):
        def run(self,obj,chars):return int(cpp(self.state,obj)==cstr(self.state,chars))
    project.hook(b+0x7e7100,Ctor());project.hook(b+0xb8f38,Equal())
    state=project.factory.blank_state(add_options=opts)
    def call(addr,state,*args):
        f=project.factory.callable(b+addr,base_state=state,concrete_only=True);result=f(*args)
        assert f.result_state is not None;return f.result_state,int(f.result_state.solver.eval(result))
    enum_results=[]
    for index,code in enumerate(LANGUAGE_CODES):
        probe=state.copy();writecpp(probe,0x70000000,code)
        probe,value=call(0x3c0040,probe,0x70000000)
        assert value==index,(code,value)
        probe.regs.x8=claripy.BVV(0x70001000,64)
        result,_=call(0x3bf61c,probe,index)
        assert cpp(result,0x70001000)==code,(index,cpp(result,0x70001000))
        enum_results.append({'code':code,'index':value})
    for invalid in [10,0xffffffff]:
        probe=state.copy();probe.regs.x8=claripy.BVV(0x70001000,64)
        result,_=call(0x3bf61c,probe,invalid)
        assert cpp(result,0x70001000)=='en'
    probe=state.copy();writecpp(probe,0x70000000,'xx');_,value=call(0x3c0040,probe,0x70000000);assert value==0
    events=[]
    class Terminal(angr.SimProcedure):
        def run(self):self.exit(0)
    def fragment(addr,probe):
        probe.regs.pc=claripy.BVV(b+addr,64);sm=project.factory.simulation_manager(probe);sm.run(n=400)
        assert not sm.active and not sm.errored and len(sm.deadended)==1,(hex(addr),sm.errored,len(sm.active),len(sm.deadended))
        return sm.deadended[0]
    class Option(angr.SimProcedure):
        def run(self,obj,text):events.append(cstr(self.state,text));self.exit(0)
    project.hook(b+0x6dea70,Option())
    for start in [0x590448,0x5eb0b8]:fragment(start,state.copy())
    assert len(events)==2 and all(e.split('\n')[-1]=='Türkçe' and len(e.split('\n'))==10 for e in events)
    project.hook(b+0x664a64,Terminal())
    welcome_results=[]
    for current in range(10):
        probe=state.copy();probe.regs.x19=claripy.BVV(0x70002000,64);probe.regs.sp=claripy.BVV(0x7fff0000,64)
        probe.memory.store(0x700020a0,struct.pack('<I',current))
        result=fragment(0x664a38,probe)
        value=result.solver.eval(result.regs.w0);text=cstr(result,result.regs.x23)
        assert value==(current+1)%10 and text==m['welcome_text'][value]
        welcome_results.append({'before':current,'after':value,'text':text})
    wizard_events=[];wizard_index=0
    class Index(angr.SimProcedure):
        def run(self,value):return wizard_index
    class Log(angr.SimProcedure):
        def run(self):return 0
    class Instance(angr.SimProcedure):
        def run(self):return 0x70004000
    class Setter(angr.SimProcedure):
        def run(self,obj,value):wizard_events.append(cpp(self.state,value));self.exit(0)
    class Invalid(angr.SimProcedure):
        def run(self):wizard_events.append('invalid');self.exit(0)
    project.hook(b+0x9f320,Index());project.hook(b+0x2395ac,Log());project.hook(b+0x3c5358,Instance());project.hook(b+0x3c0098,Setter());project.hook(b+0x67006c,Invalid())
    for wizard_index in range(11):
        probe=state.copy();probe.regs.x20=claripy.BVV(0x70003000,64);probe.regs.sp=claripy.BVV(0x7fff0000,64)
        fragment(0x670058,probe)
    assert wizard_events==LANGUAGE_CODES+['invalid'],wizard_events
    return {'passed':True,'engine':f'angr {angr.__version__} / native AArch64','ten_bidirectional_locale_mappings':enum_results,'invalid_indices_and_unknown_code_use_english':True,'settings_option_callers_checked':2,'welcome_cycle':welcome_results,'wizard_events':wizard_events,'scope':'Native registration/index mapping/menu code fragments with isolated external string, logging, and UI callbacks'}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',type=Path,default=SOURCE,help='unmodified official HelixScreen v1.0.0 U1 executable, SHA-256 locked')
    parser.add_argument('--output',type=Path,default=OUTPUT,help='destination executable or existing patched executable with --verify')
    parser.add_argument('--patch-manifest',type=Path,default=MANIFEST)
    parser.add_argument('--verification-report',type=Path,default=REPORT)
    parser.add_argument('--verify',action='store_true',help='independently reopen and verify existing output without rebuilding')
    args=parser.parse_args()
    SOURCE=args.source.resolve();OUTPUT=args.output.resolve();MANIFEST=args.patch_manifest.resolve();REPORT=args.verification_report.resolve()
    if SOURCE==OUTPUT:parser.error('source and output must be separate paths')
    if args.verify:
        manifest=json.loads(MANIFEST.read_text(encoding='utf-8'))
        verify(SOURCE.read_bytes(),OUTPUT.read_bytes(),manifest)
    else:patch()
