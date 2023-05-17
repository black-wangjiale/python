def test_func(computer):
    result=computer(1,2)
    print(result)

def computer(x,y):
    return x+y
#也可以通过lambda关键字，传入一个一次性使用的lambda匿名函数
def test_func(computer):
    result=computer(1,2)
    print(result)
test_func(lambda x,y:x+y)
#lambada格式lambda 参数：函数体，因为是匿名所以只能用一次