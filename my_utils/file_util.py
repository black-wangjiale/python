def print_file_info(file_name):
    """
    功能是：将给定路径的文件内容输出到控制台中
    ：param file_name:即将读取文件路径
    ：return：None
    """
    f=None
    try:
        f=open(file_name,"r",encoding="utf-8")
        content=f.read()
        print("文件的全部内容如下:")
        print(content)
    except Exception as e:
        print("程序出现异常，原因是：{e}")
    finally:
        # if f:          如果变量是none
        if f:
            f.close()
def append_to_file(file_name,data):
    """
    功能：将指定的数据追加到文件中
    ：param file_name:指定文件路径
    “param data：指定的数据
    ：return：None
    """
    f=open(file_name,"a",encoding="utf-8")
    f.write(data)
    f.write("\n")
    f.close()
if __name__ == '__main__':
    append_to_file("D:/wangjiale.txt","hahahhaha")