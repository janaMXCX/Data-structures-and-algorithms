"""lenght=input('输入长度:')
width=input('输入宽:')
high=input('输入高:')
V=float(lenght)*float(width)*int(high)
print('体积为',V)"""



"""a=int(input('请输入一个数:'))
x=int(input("输入的三位数的百位数字:"))
y=int(input("输入的三位数的十位数字:"))
z=int(input("输入的三位数的个位数字:"))

a=int(input('请输入一个数:'))
x=a%f
y=a//10%10
z=a//100
if x**3+y**3+z**3==a:
    print("为水仙花数")
else:
    print("不是水仙花数")"""




"""d="yes"
while d=="yes":
    a=input('请输入第一个数:')
    b=input("请输入第二个数:")
    c=input("请输入运算符:")
    if (a.find(".")):
        x=float(a)
    else:
        x=int(a)

    if (b.find(".")):
        y=float(b)
    else:
        y=int(b)

    if c=="+":
        print("结果为:",x+y)
        d=input("是否继续(yes/no):")
    elif c=="-":
        print("结果为:",x-y)
        d=input("是否继续(yes/no):")
    elif c=="*":
        print("结果为:",x*y)
        d=input("是否继续(yes/no):")
    elif c=="/":
        print("结果为:",x/y)
        d=input("是否继续(yes/no):")
    elif c=="**":
        print("结果为:",x**y)
        d=input("是否继续(yes/no):")
    elif c=="%":
        print("结果为:",x%y)
        d=input("是否继续(yes/no):")
    elif c=="//":
        print("结果为:",x//y)
        d=input("是否继续(yes/no):")
    else:
        print("您输入了非法字符")
        d=input("是否继续(yes/no):")
else:
    print("结束计算")"""



def sum(i,a,b):
    if i=="*":
        x=a*b
    elif i=="+":
        x=a+b
    elif i=="-":
        x=a*b
    elif i=="/":
        x=a/b
    return x

d = "yes"
while d=="yes":
    m = input("请输入第一个数:")
    n = input("请输入运算符:")
    v = input("请输入第二个数:")
    result = sum(n,m,v)
print(result)


    









