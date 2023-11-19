#循环正常执行完就会执行else
#如果遇到break那么else就不会执行
b=3
for a in range(3):
    pwd=input("请输入密码:")
    if pwd=="2636662631":
        print("密码正确")
        break
    else:
        b-=1 and b>=1
        print("密码错误，你还有"+str(b)+"次机会")
else:
    print("对不起，三次输入密码均错误")

#和 while 一起使用
c=0
while c<3:
    pwd=input("请输入密码:")
    if pwd=="2636662631":
        print("密码正确")
        break
    else:
        print('密码错误')
        c+=1
else:
    print("对不起，验证失败")

