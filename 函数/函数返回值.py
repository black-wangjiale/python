def test(num1,num2):
    result=num1+num2
    return result
    #return后续代码不会被执行

res=test(1,2)
print(res)

def measure():
    #量体温

    print("开始测量体温")
    temp1=36.3
    temp2=38
    print("测量结束")
    return (temp1,temp2)#可以返回一个元组，让元组元素返回数据且元组小括号可以去掉
result1,result2=measure()
print(result1)
print(result2)

