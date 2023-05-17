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



print(len(name_list))#len用来计算集合里有多少个元素
print(name_list.count(1))