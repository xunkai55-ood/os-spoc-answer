# 07-1 SPOC Answer

2012011486 张洵恺

2012013290 韩珊

## Bakery算法若无choosing

如果没有choosing，可能会发生错误。举例如下：

设有进程a，b（`pid(a) == i < pid(b) == j`），初始时`NUM[i] = NUM[j] = 0`。

a执行到`MAX( ... ) + 1`，在赋值之前切换到b。此时`NUM[i] == NUM[j] == 0`。

b执行完`MAX( ... ) + 1`。此时`NUM[i] == 0, NUM[j] == 1`。b进入临界区。

此时又切换回a，完成赋值，此时`NUM[i] == 1, NUM[j] == 1`。由于NUM相同，i < j，a也进入临界区。

