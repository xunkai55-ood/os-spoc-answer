# 04-1 SPOC Answer

张洵恺 2012011486

韩珊 2012013290

## Translation

代码见[convert.py](04-1-answer/convert.py)

运行时，需要在os-spoc-answer项目根目录下，执行

```
python 04-1-answer/convert.py
```

## Answer

```
6653
	invalid pde

1c13
	pde valid 1, pfn 0x3d
		pte valid 1, pfn 0x76
			physical address = 0xed3
				value = 0x12
				
6890
	invalid pde

af6
	pde valid 1, pfn 0x21
		pte valid 0, pfn 0x7f
			disk sector address = 0xff6
				value = 0x3

1e6f
	pde valid 1, pfn 0x3d
		pte valid 0, pfn 0x16
			disk sector address = 0x2cf
				value = 0x1c
```


