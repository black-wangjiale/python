#定义远足
t1=()#空元组
#元组拆包装包
t1=(9,7,4,6,3,1)
a,*_,b=t1#先让固定的变量来接受元素，*——来接受剩下的元素，以列表的形式存在
print(a)
print(_)#去掉*就是装包
print(*_)
print(b)
x,y,*z="hello"#字符串拆包装包
print(x,y,z)
print(*z)


#元组运算符 + * is in
#类型转换
list_1=[]
tuple1=tuple(list_1)#把列表转换成元组
list1=list(tuple1)#把元组转换成列表
#取值
#查询下标 index来取值，或者切片[：：]
#关于元组的函数：max(),min(),sum(),len()
#关于元组的方法.index .count 


#sorted()能排序吗？
t5=(4,2,434,43,54)
print(sorted(t5))#直接打印出一个排序后的列表
result=t5.index(434)
print(result)