#_*_coding:utf-8_*_
print("欢迎来到黑马动物园")
height=int(input("请输入你的身高："))
vip_level=int(input("请输入你的vip等级:"))
if height<120:
    print("身高小于120,可以免费")
elif vip_level>3:
    print("VIP级别大于3,可以免费！")
else:
    print("不好意思，条件都不满足，需要买票！")