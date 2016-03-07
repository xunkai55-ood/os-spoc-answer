# 03-1 SPOC Answer

实现了最简单的first-fit算法。

代码在[malloc.c](03-1-answer/malloc.c)。

### 设计思路

每个block对应一个block info结构体，记录该block的起点（相对于heap的偏差）和大小。方便起见，block info是用链表中的节点（block node）代替的，因此会有一个域记录下一个block node在内存中的位置。

换句话说，对于所有空闲块，**在其开始的位置**，有一个16B的空间用于存储块的信息（起点、大小、在free block list中下一个块的位置）。对于所有已分配的块，也会有同样大小的16B空间（也是在块开始）记录块信息，但其中有8B的信息是无用的。

程序开始时，内存被分为一个块，当然也是空闲块。每当有分配内存请求的时候，就会在free block list中寻找第一个“能放得下的”块。free block list是按照起点升序排列的。

找块分为以下三种情况（以下的block_size均不包括头部的info的大小）：

1. 找到一个`block_size > request_size + BLOCK_INFO_SIZE`的块。将该块的后面的`request_size + BLOCK_INFO_SIZE`的部分截出，在头部创建一个block info，将剩余部分作为alloc的结果返回；
2. 找到一个`request_size + BLOCK_INFO_SIZE >= block_size >= request_size`的块。将这个块移出free block list，其对应的空间作为结果返回。
3. 什么都没找到，说明此时应该进行碎片整理。

释放空间比较简单，首先弱判断了释放的是不是一个malloc分配出的空间的头部（若是，该地址往前的16B应该是一个block info），然后将块移回free block list。**这个实现中，没有进行相邻空闲块的合并**。

### 试运行

在主程序中代码如下：
```
show_free_list();
char *a1 = ff_malloc(100);  // a1
show_free_list();
char *a2 = ff_malloc(80);  // a1, a2
show_free_list();
char *a3 = ff_malloc(100);  // a1, a2, a3
show_free_list();
ff_free(a2);
show_free_list();
char *a4 = ff_malloc(50);
show_free_list();
char *a5 = ff_malloc(550);
show_free_list();
char *a6 = ff_malloc(50);
show_free_list();
char *a7 = ff_malloc(48);
show_free_list();
char *a8 = ff_malloc(30);
show_free_list();
return 0;
```

对应的结果如下：

```
$ ./malloc
(16, 1008)
=======
(16, 892)
=======
(16, 796)
=======
(16, 680)
=======
(16, 680) (828, 80)
=======
(16, 614) (828, 80)
=======
(16, 48) (828, 80)
=======
(16, 48) (828, 14)
=======
(828, 14)
=======
No available memory. GC would start(828, 14)
=======
```

解释

1. 开始时，总大小1024B，抛去16B的头，free list中只有一个块：从0x10开始的1008B的空闲块。
2. 依次申请100B、80B、100B的空间。由于每次分割是把后面的部分分割出来，因此可以看到1008B的空闲块不断缩小116B、96B、116B。内存中结构大致为“空闲块-a3-a2-a1”。
3. 释放a2。内存结构为“空闲块(16+680)-a3-空闲块2(16+80)-a1”。
4. 申请a4。free block list升序排列，因此虽然a4可以放入第二个空闲块，但还是按照first-fit的要求切割了更大的空闲块1。内存结构变为“空闲块-a4-a3-空闲块-a1”。
5. 申请a5。内存结构变为“空闲块-a5-a4-a3-空闲块-a1”。
6. 申请a6。此时第一个空闲块放不下a6（48 < 50），因此第二个空闲块的后半部分被切掉给了a6。
7. 申请a7。a7大小正好可以用第一个空闲块，因此第一个空闲块整个移出了free block list。
8. 申请a8，空间不够，触发警告。内存结构不变。


