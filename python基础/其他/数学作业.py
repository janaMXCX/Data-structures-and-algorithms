lst=[]#姓名列表
lst2=[]#成绩列表
lst3=[]#等级列表

x=int(input('请输入要录入的人数:'))
for a in range(0,x):
    b=input('请输入姓名:')
    c=int(input('请输入其成绩:'))
    lst.append(b)
    lst2.append(c)
#创建两个列表，分别与姓名成绩有关
'''print(lst)
print(lst2)'''
d={lst:lst2 for lst,lst2 in zip(lst,lst2)}#学生姓名成绩的字典
for i in lst2:
    if i>=90:
        g='优秀'
    elif  80<=i<=89:
        g='良好'
    elif 70<=i<=79:
        g='中等'
    elif 60<=i<=69:
        g='及格'
    elif i<60:
        g='不及格'
    lst3.append(g)#lst3为成绩等级的划分

sum=0
for m in lst2:
    sum+=m
p=sum/x

print('姓名:\t',lst)
print('成绩:\t',lst2)
print('等级:\t',lst3)
print('平均成绩为:',p)
lst2.sort(reverse=True)
print('最高分为:',lst2[0])
lst2.sort(reverse=False)
print('最低分为:',lst2[0])


    
