name_list=["张三","王五","李四"]
name_list.append("哈利波特")
print(name_list)
name_list.insert(3,"伏地魔")
print(name_list)
name_list.extend(name_list) 
print(name_list)
name_list.remove("张三")
name_list.pop(2)#不加索引默认移除第一个元素
print(name_list)
del name_list[0]


num_list=[1,2,3,4,5,6,1,4,23,25]
print(len(num_list))#len用来计算集合里有多少个元素
print(num_list.count(1))#.count用来计算元素的个数
print(num_list.sort())#.sort升序
print(num_list.reverse())#.reverse逆序
