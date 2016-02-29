# 02-1 SPOC Answer

张洵恺 2012011486

韩珊 2012013290

### 3.4 linux系统调用分析

#### 通过分析lab1-ex0了解Linux应用的系统调用编写和含义。

编译好lab1-ex0后运行，发现这是一个“Hello World”程序。

**objdump**是常用的反汇编工具，能自动识别应用程序文件格式，生成对应的汇编代码。通过`objdump -S lab1-ex0.exe > lab1-ex0.objdump.s`可以得到该汇编代码。

**nm**可以用来显示目标文件的符号表。通过`nm lab1-ex0.exe > lab1-ex0.nm.txt`可以得到符号表。

**file**通过识别文件头部的信息，来判断文件的类型。
```
$ file lab1-ex0.exe lab1-ex0.exe: ELF 32-bit LSB  executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=0116e16f94edba92fbcda8d2b011fb0177e85c50, not stripped```

**strace**常用来跟踪进程执行时的系统调用和所接收的信号。增加f选项可以查看包括fork出的进程在内的所有内容。通过`strace -f ./lab1-ex0.exe &> lab1-ex0.strace.txt`可以保存结果。

使用strace后可以发现这个小程序进行了茫茫多的系统调用，其中大部分为open("something.so")，判断这是打开动态链接库所需要的系统调用。其中还有access调用，检查了/etc/ld.so.nohwcap文件是否存在（经查资料，这是给链接器判断是否要进行优化的）。fstat获取文件状态。read读取文件（判断是读取了可执行文件）。mmap2进行内存地址空间映射。munmap取消映射。exit_group退出所有进程。

用户的应用程序真正的逻辑是write调用，将hello world输出。

#### 通过调试lab1_ex1了解Linux应用的系统调用执行过程。

`strace -c`进行了系统调用相关的统计。从左到右，各列依次为时间开销百分比、秒数，平均每次调用的微秒数，调用次数和调用出错的次数。
```
$ strace -c ./lab1-ex1.exehello world% time     seconds  usecs/call     calls    errors syscall------ ----------- ----------- --------- --------- ----------------  0.00    0.000000           0         1           read  0.00    0.000000           0         1           write  0.00    0.000000           0        10         8 open  0.00    0.000000           0         2           close  0.00    0.000000           0         8         7 stat  0.00    0.000000           0         3           fstat  0.00    0.000000           0         8           mmap  0.00    0.000000           0         4           mprotect  0.00    0.000000           0         1           munmap  0.00    0.000000           0         1           brk  0.00    0.000000           0         3         3 access  0.00    0.000000           0         1           execve  0.00    0.000000           0         1           arch_prctl------ ----------- ----------- --------- --------- ----------------100.00    0.000000                    44        18 total
```





