f=open("D:/wangjiale.txt","r",encoding="utf-8")
""" 
print(f"读取十个字节的结果：{f.read(10)}")
print(f"读取全部内容的结果是:{f.read()}")#连续调用两次read下一个read会到下一个read后读取
lines=f.readlines()#读取文件的全部行，封装到列表中
print(f"lines对象的内容是{lines}") 
"""
""" line1=f.readline()
line2=f.readline()
line3=f.readline()
print(f"line1的内容是{line1}")
print(f"line2的内容是{line2}")
print(f"line3的内容是{line3}")
#for循环读取文件行 """
for line in f:
    print(f"每一行的内容是:{line}")
f.close()