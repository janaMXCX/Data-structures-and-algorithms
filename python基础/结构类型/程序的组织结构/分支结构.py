"""
程序根据判断条件的布尔值选择性的执行部分代码
明确让计算机知道在什么条件下，该去做什么
"""
#1.单分支结构
#中文语义：如果...就...
#if 条件表达式
#   条件执行体
money=1000 #余额
a=int(input('请输入取款金额：')) #取款金额
#判断余额是否充足
if money>=a:
    money=money-a
    print("取款成功，余额为：",money)
#2.双分支结构
#中文语义 如果......不满足......就......
num=int(input('输入一个整数：'))
#判断条件
if num%2==0:
    print(num,'是偶数')
else:
    print(num,'是奇数')
#多分支结构
"""
中文语义：是...吗？不是
         是...吗？不是
         是...吗？不是
         是...吗？是
"""
'''
if 条件表达式1-->条件执行体1
elif条件表达式2-->条件执行体2
elif条件表达式3-->条件执行提3
[else:]条件执行体N+1
'''
"""
从键盘录入一个成绩 整数
90-100 A
80-89 B
70-79 C
60-69 D
0-59 E
小于0或者大于100为非法数据(不是成绩的有限范围)
"""
score=int(input('请输入一个成绩:'))
#判断
if score>=90 and score<=100:
    print('A级')
elif score>=80 and score<=89:
    print('B级')
elif score>=70 and score<=79:
    print('C级')
elif score>=60 and score<=79:
    print('D级')
elif score>=0 and score<=59:
    print('E级')
else:
    print("对不起，你的成绩不在有效范围")
#也可以像下面一样书写
score=int(input('请输入一个成绩:'))
#判断
if 90<=score<=100:
    print('A级')
elif 80<=score<=89:
    print('B级')
elif 70<=score<=79:
    print('C级')
elif 60<=score<=79:
    print('D级')
elif 0<=score<=59:
    print('E级')
else:
    print("对不起，你的成绩不在有效范围")


#嵌套if
answer=input("你是会员吗？")
money=float(input("请输入您的购物金额:"))
if answer=="y":
    if money>=200:
        print('打八折，付款金额为:',money*0.8)
    elif 100<=money<=199:
        print('打九折，付款金额为:',money*0.9)
    else:
        print('不打折，付款金额为:',money)
else:
    if money>=200:
        print('打九五折，付款金额为',money)
    else:
        print('不打折，付款金额为:',money)

#条件表达式
a=int(input('输入第一个整数'))
b=int(input('输入第二个整数'))
print((str(a)+'大于等于'+str(b)) if a>=b else (str(a)+'小于'+str(b)))