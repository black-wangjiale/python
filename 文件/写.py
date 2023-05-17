f=open("D:/hacker.txt","w",encoding="utf-8")#w模式下如果有文件就清空原有文件，若国没文件就新建文件
f.write("我无敌你随意！")#将内容写入缓冲区，用flush将文件写入硬盘
f.flush()
f.close()#close内置flush功能