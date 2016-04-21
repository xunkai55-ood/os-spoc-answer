# 06-2 SPOC Answer

2012011486 张洵恺

2012013290 韩珊

## 溢出问题的解决

我们注意到，STRIDE值是在0附近变化的数，因此我们可以把它当做有符号整数进行比较，当做无符号整数进行计算。这样的话，比较的“突变”会发生在无符号整数最大值一半的地方，而不是0和-1之间。只要设置合理的PASS_MAX，STRIDE和PASS值就不会接触到突变的位置，就可以保证变化的连续性，避免出错。

## STRIDE算法输出信息

代码见[lab6](06-2-answer)

```
++ setup timer interrupts
[pick] pid=1, stride=2147483647
[deq] pid=1 stride=2147483647 priority=0
[enq] pid=2 stride=0 priority=0
[pick] pid=2, stride=2147483647
[deq] pid=2 stride=2147483647 priority=0
kernel_execve: pid = 2, name = "exit".
I am the parent. Forking the child...
[enq] pid=3 stride=0 priority=0
I am parent, fork a child pid 3
I am the parent, waiting now..
[pick] pid=3, stride=2147483647
[deq] pid=3 stride=2147483647 priority=0
I am the child.
[enq] pid=3 stride=2147483647 priority=0
[pick] pid=3, stride=-2
[deq] pid=3 stride=-2 priority=0
[enq] pid=3 stride=-2 priority=0
[pick] pid=3, stride=2147483645
[deq] pid=3 stride=2147483645 priority=0
[enq] pid=3 stride=2147483645 priority=0
[pick] pid=3, stride=-4
[deq] pid=3 stride=-4 priority=0
[enq] pid=3 stride=-4 priority=0
[pick] pid=3, stride=2147483643
[deq] pid=3 stride=2147483643 priority=0
[enq] pid=3 stride=2147483643 priority=0
[pick] pid=3, stride=-6
[deq] pid=3 stride=-6 priority=0
[enq] pid=3 stride=-6 priority=0
[pick] pid=3, stride=2147483641
[deq] pid=3 stride=2147483641 priority=0
[enq] pid=3 stride=2147483641 priority=0
[pick] pid=3, stride=-8
[deq] pid=3 stride=-8 priority=0
[enq] pid=2 stride=2147483647 priority=0
[pick] pid=2, stride=-2
[deq] pid=2 stride=-2 priority=0
waitpid 3 ok.
exit pass.
[enq] pid=1 stride=2147483647 priority=0
[pick] pid=1, stride=-2
[deq] pid=1 stride=-2 priority=0
[enq] pid=1 stride=-2 priority=0
[pick] pid=1, stride=2147483645
[deq] pid=1 stride=2147483645 priority=0
all user-mode processes have quit.
init check memory pass.
kernel panic at kern/process/proc.c:460:
    initproc exit.

Welcome to the kernel debug monitor!!
Type 'help' for a list of commands.
```


