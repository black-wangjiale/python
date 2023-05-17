from __future__ import print_function


def func(num,num_list):
    print("函数内部")
    num=99#不可变类型使用global
    num_list+=[8,8,8]#可变类型在函数内部可使用方法改变外部
    #+=就是num_list.extend([8,8,8])

    print(num)
    print(num_list)


gl_num=9
gl_num_list=[4,5,6]
func(gl_num,gl_num_list)
print(gl_num)
print(gl_num_list)

def print_info(name,gender=True):#缺省参数使用最常见的值
    """
    :pram name:班上同学的姓名
    :pram gender:Ture 男生 Flase 女生
    """
    gender_text="男生"
    if not gender:
        gender_text="女生"
    print("{}是{}".format(name,gender_text))

print_info("乐乐侠")
print_info("小红")

    
