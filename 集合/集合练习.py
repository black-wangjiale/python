my_list=["theshy","rookie","ning","jackeylove","baolan"]
my_set2={"xiaoming","xiaohu","ning"}
my_list.append("theshy")
my_set=set()
for i in my_list:
    my_set.add(i)
print(my_set)
#my_set.remove("theshy")
#result=my_set.pop()#随机取出一个元素，该元素不在原集合中了
#print(result)q
my_set.difference(my_set2)#得到两个集合的差集
print(my_set)
my_set.difference_update(my_set2)#消除两个集合的差集
print(my_set)
my_set4=my_set.union(my_set2)#并集
print(my_set4)