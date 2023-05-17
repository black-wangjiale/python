nmum=10

def demo1():
    global num#希望改变全局变量的值,在函数内部使用global来进行修改
    num=100
    print("demo--->%d" % num)
def demo2():
    print("demo--->%d" % num)
demo1()
demo2()

