'''不可变序列以及可变序列'''
#可变序列“列表，字典”更改之后内存地址不发生改变
#不可变序列“字符串，元组”更改之后，内存地址会改变
t=('python','hello',90)#这个就是元组
#创建元组的方式可以直接用小括号创建
#可以使用内置函数tuple()创建
b=tuple(('python','hello',90))
print(b,type(b))
#只包含一个元素需要用到逗号和小括号 
a=('python',)
print(a,type(a))
#也可以省略小括号进行操作
c='python','hello',98
print(c,type(c))
d='python',
print(d,type(d))


'''创建方法'''
lst=[]
lst1=list()
#列表的创建方法
d={}
d2=dict()
#字典的创建方法。

#空元组
t4=()
t5=tuple()
#在多任务情况下，尽可能使用不可变序列，同时操作对象时不需要加锁
#元组中存储的是对象的引用
'''元组中的元素不可以改变，但是元组中的可变量（此处为列表，字典等，同时进行添加操作之后列表地址不变）是可以进行增加操作的'''