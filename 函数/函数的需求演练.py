def print_line(char,times):
    #打印分割线

    print(char*times)
print_line("!",100)


def print_lines(char,times,lines):
    #打印多行分割线
    for i in range(lines):
        print_line(char,times)
print_lines("$",100,5)