#计算一到一百之间的偶数和
#初始变量
sum=0  #用于存储偶数和
a=1
#判断挑条件
while a<=100:
    #条件执行体(求和)
    if not bool(a%2):  #也可以写成if a%2:  因为他有自己的布尔值0的布尔值为false此时条件不成立循环会变为求奇数和。
        sum+=a
    #改变变量
    a+=1
print('1到100之间的偶数和为:',sum)