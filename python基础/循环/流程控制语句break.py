#通常用于结束循环结构，通常与分支结构if一起使用。
#非正常结束循环
#从键盘录入密码，最多录入三次，如果正确就停止录入。
for a in range(3):
    pwd=input("请输入密码:")
    if pwd=="2636662631":
        print("密码正确")
        break
    else:
        print("密码不正确")


a=0
while a<3:
    pwd=input("请输入密码")
    if pwd=="2636662631":
        print("密码正确")
        break
    else:
        print("密码错误")
        a+=1