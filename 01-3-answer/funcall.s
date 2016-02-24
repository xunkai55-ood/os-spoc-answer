funcall.c  1: #include <u.h>
root/lib/u.h  1: // u.h
root/lib/u.h  2: 
root/lib/u.h  3: // instruction set
root/lib/u.h  4: enum {
root/lib/u.h  5:   HALT,ENT ,LEV ,JMP ,JMPI,JSR ,JSRA,LEA ,LEAG,CYC ,MCPY,MCMP,MCHR,MSET, // system
root/lib/u.h  6:   LL  ,LLS ,LLH ,LLC ,LLB ,LLD ,LLF ,LG  ,LGS ,LGH ,LGC ,LGB ,LGD ,LGF , // load a
root/lib/u.h  7:   LX  ,LXS ,LXH ,LXC ,LXB ,LXD ,LXF ,LI  ,LHI ,LIF ,
root/lib/u.h  8:   LBL ,LBLS,LBLH,LBLC,LBLB,LBLD,LBLF,LBG ,LBGS,LBGH,LBGC,LBGB,LBGD,LBGF, // load b
root/lib/u.h  9:   LBX ,LBXS,LBXH,LBXC,LBXB,LBXD,LBXF,LBI ,LBHI,LBIF,LBA ,LBAD,
root/lib/u.h  10:   SL  ,SLH ,SLB ,SLD ,SLF ,SG  ,SGH ,SGB ,SGD ,SGF ,                     // store
root/lib/u.h  11:   SX  ,SXH ,SXB ,SXD ,SXF ,
root/lib/u.h  12:   ADDF,SUBF,MULF,DIVF,                                                   // arithmetic
root/lib/u.h  13:   ADD ,ADDI,ADDL,SUB ,SUBI,SUBL,MUL ,MULI,MULL,DIV ,DIVI,DIVL,
root/lib/u.h  14:   DVU ,DVUI,DVUL,MOD ,MODI,MODL,MDU ,MDUI,MDUL,AND ,ANDI,ANDL,
root/lib/u.h  15:   OR  ,ORI ,ORL ,XOR ,XORI,XORL,SHL ,SHLI,SHLL,SHR ,SHRI,SHRL,
root/lib/u.h  16:   SRU ,SRUI,SRUL,EQ  ,EQF ,NE  ,NEF ,LT  ,LTU ,LTF ,GE  ,GEU ,GEF ,      // logical
root/lib/u.h  17:   BZ  ,BZF ,BNZ ,BNZF,BE  ,BEF ,BNE ,BNEF,BLT ,BLTU,BLTF,BGE ,BGEU,BGEF, // conditional
root/lib/u.h  18:   CID ,CUD ,CDI ,CDU ,                                                   // conversion
root/lib/u.h  19:   CLI ,STI ,RTI ,BIN ,BOUT,NOP ,SSP ,PSHA,PSHI,PSHF,PSHB,POPB,POPF,POPA, // misc
root/lib/u.h  20:   IVEC,PDIR,SPAG,TIME,LVAD,TRAP,LUSP,SUSP,LCL ,LCA ,PSHC,POPC,MSIZ,
root/lib/u.h  21:   PSHG,POPG,NET1,NET2,NET3,NET4,NET5,NET6,NET7,NET8,NET9,
root/lib/u.h  22:   POW ,ATN2,FABS,ATAN,LOG ,LOGT,EXP ,FLOR,CEIL,HYPO,SIN ,COS ,TAN ,ASIN, // math
root/lib/u.h  23:   ACOS,SINH,COSH,TANH,SQRT,FMOD,
root/lib/u.h  24:   IDLE
root/lib/u.h  25: };
root/lib/u.h  26: 
root/lib/u.h  27: // system calls
root/lib/u.h  28: enum {
root/lib/u.h  29:   S_fork=1, S_exit,   S_wait,   S_pipe,   S_write,  S_read,   S_close,  S_kill,
root/lib/u.h  30:   S_exec,   S_open,   S_mknod,  S_unlink, S_fstat,  S_link,   S_mkdir,  S_chdir,
root/lib/u.h  31:   S_dup2,   S_getpid, S_sbrk,   S_sleep,  S_uptime, S_lseek,  S_mount,  S_umount,
root/lib/u.h  32:   S_socket, S_bind,   S_listen, S_poll,   S_accept, S_connect, 
root/lib/u.h  33: };
root/lib/u.h  34: 
root/lib/u.h  35: typedef unsigned char uchar;
root/lib/u.h  36: typedef unsigned short ushort;
root/lib/u.h  37: typedef unsigned int uint;
root/lib/u.h  38: 
funcall.c  2: int ret;
funcall.c  3: out(port, val)
funcall.c  4: {
funcall.c  5:   asm(LL,8);   // load register a with port
00000000  0000080e  LL    0x8 (D 8)
funcall.c  6:   asm(LBL,16); // load register b with val
00000004  00001026  LBL   0x10 (D 16)
funcall.c  7:   asm(BOUT);   // output byte to console
00000008  0000009a  BOUT
funcall.c  8: }
funcall.c  9: 
funcall.c  10: int write(int f, char *s, int n)
0000000c  00000002  LEV   0x0 (D 0)
funcall.c  11: {
funcall.c  12:   int i;
funcall.c  13:   ret = 1;
00000010  fffff801  ENT   0xfffffff8 (D -8)
00000014  00000123  LI    0x1 (D 1)
00000018  00000045  SG    0x0 (D 0)
funcall.c  14:   i=n;
0000001c  0000200e  LL    0x20 (D 32)
00000020  00000440  SL    0x4 (D 4)
funcall.c  15:   while (i--)
00000024  00000003  JMP   <fwd>
funcall.c  16:     out(f, *s++);
00000028  0000180e  LL    0x18 (D 24)
0000002c  ffffff57  SUBI  0xffffffff (D -1)
00000030  00001840  SL    0x18 (D 24)
00000034  ffffff1f  LXC   0xffffffff (D -1)
00000038  0000009d  PSHA
0000003c  0000180e  LL    0x18 (D 24)
00000040  0000009d  PSHA
00000044  ffffb805  JSR   0xffffffb8 (TO 0x0)
00000048  00001001  ENT   0x10 (D 16)
funcall.c  17:   return i;
0000004c  0000040e  LL    0x4 (D 4)
00000050  00000157  SUBI  0x1 (D 1)
00000054  00000440  SL    0x4 (D 4)
00000058  00000154  ADDI  0x1 (D 1)
0000005c  00000086  BNZ   <fwd>
00000060  0000040e  LL    0x4 (D 4)
00000064  00000802  LEV   0x8 (D 8)
funcall.c  18: }  
funcall.c  19: 
funcall.c  20: main()
00000068  00000802  LEV   0x8 (D 8)
funcall.c  21: {
funcall.c  22: 
funcall.c  23:   //Change S1/S2 ID to your student ID, and change 12 to new str length
funcall.c  24:   ret = write(1, "2012011486 2012013290", 22);
0000006c  0000169e  PSHI  0x16 (D 22)
00000070  00000008  LEAG  0x0 (D 0)
00000074  0000009d  PSHA
00000078  0000019e  PSHI  0x1 (D 1)
0000007c  ffff9005  JSR   0xffffff90 (TO 0x10)
00000080  00001801  ENT   0x18 (D 24)
00000084  00000045  SG    0x0 (D 0)
funcall.c  25:   asm(HALT);
00000088  00000000  HALT
funcall.c  26: }
funcall.c  27: 
0000008c  00000002  LEV   0x0 (D 0)
