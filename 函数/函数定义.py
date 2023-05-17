#定义一个函数
def mutiple_table():
    i=1
    while i<=9:
        j=1
        while j<=i:
            print("{}*{}={}".format(j,i,i*j),end="\t")
            j+=1
        print("")#什么都不打印，但是换行
        i+=1

#调用函数
#mutiple_table()

def say_hello():
    print("hello!")