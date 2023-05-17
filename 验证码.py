string="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
code=""
import random
for i in range(4):
    ran=random.randint(0,len(string)-1)
    code+=string[ran]

print("验证码是：{}".format(code))
#提示用户输入验证码（输入的时候忽略大小写）
user_input=input("请输入验证码：")
if user_input.lower() and code.lower():
    print("验证码输入正确！")
else:
    print("验证码输入错误！")