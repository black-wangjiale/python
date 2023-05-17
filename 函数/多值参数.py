#*args arguments 有变量的意思 多值的元组
#**kwargs用来接收多值的字典

def demo(num,*args,**kwargs):
    print(num)
    print(args)
    print(kwargs)

demo(1,2,3,4,5,name="张三",gender="男",age="18")

def sum_numbers(*args):
    num=0
    for n in args:#元组
        num+=n#遍历元组，将每个元组的每个元素相加
    return num

print(sum_numbers(1,2,3,4))