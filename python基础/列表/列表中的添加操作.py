#可以输入append()可以在前面的列表中的末尾添加上一个元素
lis=[3,2,10]
print('添加之前',lis)
lis.append(100)
print('添加之后',lis)
#entend()在列表的末尾至少添加一个元素
lst=['hello','word']
lis.append(lst)
print(lis)
lis.extend(lst)
print(lis)
#insert()在列表的任意位置添加一个元素
lis.insert(1,90)#在权值为1的位置添加一个90
print(lis)
lst3=[True,False,'hello']
#在任意位置添加上N多个元素
lst[1:]=lst3
print(lst)