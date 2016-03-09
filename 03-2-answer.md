# 03-2 SPOC Answer

2012011486 张洵恺

2012013290 韩珊

### 小组第二题

根据规则，选取解的两个地址为第1组：0x6c74，0x6b22。

虚拟内存大小32KB，因此虚拟地址15位。页目录表、页表大小均为32Bytes，地址各5位。虚拟地址结构=5位PDE索引+5位PTE索引+5位页内索引。

观察内存表，一个内存地址对应一个Byte，一页32Bytes，因此物理内存地址前7位为页号，后5位为偏移量。

PDBR为0x220，按上面的逻辑翻译为001000100000，页号为0x11，偏移量为0。

#### 0x6c74

将0x6c74分解为15位二进制串：110110001110100。前5位0x1b，即是PDE index，十进制为27，加上PDBR=0x220，得到PDE content=0xa0=10100000，标记位为1，合法。页帧号PFN=0x20。

地址中5位为0x3。配合前面的页帧号，得到PTE content=0xe1，第一位标记位为1合法，因此PT=0x61。

地址最后5位0x14。配合PT，为0x61页的第20个，查表得到结果0x06。

```
Virtual Address 6c74:
  --> pde index:0x1b  pde contents:(valid 1, pfn 0x20)
    --> pte index:0xe1  pte contents:(valid 1, pt 0x61)
      --> offset:0x14  Translate to Physical Address --> Value: 0x06
```

#### 0x6b22

将0x6b22分解为15位二进制串：110101100100010。PDE index=0x1a，同前题得到PDE content=d2，标记位为1合法，PFN=0x52。

地址中5位0x19。配合页帧号，得到PTE content=0xc7，第一位标记位为1合法，因此PT=0x47。

地址后5位0x2。配合PT，查标得到结果0x1a。

```
Virtual Address 6b22:
  --> pde index:0x1a  pde contents:(valid 1, pfn 0x52)
    --> pte index:0x19  pte contents:(valid 1, pt 0xc7)
      --> offset:0x2  Translate to Physical Address --> Value: 0x1a
```

### 小组第三题

程序见[convert.py](03-2-answer/convert.py)


