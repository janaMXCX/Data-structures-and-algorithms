"""def high(x):
    if x>0:
        x=1
    else:
        x=0
    return x

a=int(input("请输入a的值"))
if high(a):
    print("a为正数")
else:
    print("a为负数")"""


a1=270000//1260+1
a2=270000//2525+1

for y in range(a1):
    for z in range(a2):
        for x in range(13):
            if y*1260+z*2525+x*10000==270000:
                print("可以换1万摩拉",x,"次")
                print("可以分解三星圣遗物",y,"次")
                print("可以刷副本",z,"次")

"""import random

a=int(random.uniform(0,31))
print(a)"""


"""lst=[]
b=0
while b<1:
    a=input("请输入内容")
    if a=='Y':
        break
    lst.append(a)
lst=''.join(lst)
print(lst)
lst=list(lst)
lst.reverse()
print(lst)
"""
"""lst2=[]
b='hello python'
lst2.append(b)
print(lst2)
lst2=''.join(lst2)
print(lst2)
lst2=list(lst2)
print(lst2)
lst2.reverse()
print(lst2)"""
