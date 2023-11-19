#对变量或者表达式进行大小，真假比较
a,b=10,20
print('a>b吗?',a>b) #False
print('a<b吗?',a<b) #True
print('a<=b吗?',a<=b)
print('a>=b吗?',a>=b)
print('a==b吗?',a==b) #==表示等于
print('a!=b吗?',a!=b) #!=表示不等于
'''
一个"="称为赋值运算符
两个"=="称为比较运算符
一个变量由三部分组成,标识,类型,值
==比较的是值
比较对象的标识使用的是is
'''
a=10
b=10
print(a is not b)#a和b的id是不相等的吗?
print(a==b)#true    说明a与b的vale 相等
print(a is b)#true  说明,a与b的id标识相等
#一下代码暂时没学过
lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1==lst2)
print(lst1 is lst2)
print(id(lst1))
print(id(lst2))
print(lst1 is not lst2)
