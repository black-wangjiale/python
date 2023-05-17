filename='picture.png'
print(filename[0:5])#0是起始值，5是结束值，但是不包括5，包前不包后
print(filename[3:5])
print(filename[3:])#省略后面则一直去指导字符串末尾
print(filename[:7])#省略了前面，从0开始一直取到结束
print(filename[:])#省略首尾，取整个字符串

print(filename[8:-1])
print(filename[:-2])#等价于print(filename[:9])
print(filename[-8:])

str1="abcdad"
print(str1[-1:-5:-1])#从后往前取值，要注意改步长。
#练习 hello world
str2="hello world"
print(str2[-1:0:-1])#逆序输出hello world