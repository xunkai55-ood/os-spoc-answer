# 09-1 SPOC Answer

2012011486 张洵恺

2012013290 韩珊

完成SFS的功能。

## 根据sfs文件系统的状态变化信息，给出具体的文件相关操作内容

0. 初始化
1. 在根目录下新建了空目录g `mkdir("/g")`
2. 在根目录下新建了空文件q `create("/q")`
3. 在根目录下新建了空文件u `create("/u")`
4. 在根目录下新建了指向u的硬链接x `link("/u", "/x")`
5. 在根目录下新建了空目录t `mkdir("/t")`
6. 在目录g下新建了空文件c `create("/g/c")`
7. 解除硬链接x `unlink("/x")`
8. 在目录g下新建了空目录w `mkdir("/g/w")`
9. 在文件c中写入了一个block
10. 在根目录下新建了空文件n `create("/n")`

## 在sfs-homework.py 参考代码的基础上，实现 writeFile, createFile, createLink, deleteFile，使得你的实现能够达到与问题1的正确结果一致

实现见[代码](09-1-answer/sfs-homework.py)。

将第一问答案填入结果存到[answer.txt](09-1-answer/answer.txt)中（注意代码输出的create被打错，因此全写作creat）

运行

```
cd 09-1-answer
python sfs-homework.py > output.txt
diff output.txt answer.txt
```

结果没有差别，说明实现基本正确。

## 实现soft link机制，并设计测试用例说明你实现的正确性

实现中，增加了`createSoftLink`函数，修改了`writeFile`函数。因为后者在写向软连接时，需要进一步寻找目标文件。最大递归层数设为4，以防出现循环软链接或超长软链接等。

实现了`doSoftLink`代替了`doLink`，用于测试。

代码见[sfs-homework-2.py](09-1-answer/sfs-homework-2.py)


