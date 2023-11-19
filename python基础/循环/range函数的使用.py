#range()的创建方式
#第一种创建方式，只有一个参数(小括号只给了一个数)
r=range(10)#默认从零开始默认相差1称为步长
print(r)
print(list(r))#用于查看range对象中的整数序列  list是列表的意思

#第二种创建方式
r=range(2,12)#指定开始值以及结束值，同时步长为1
print(list(r))
#第三种创建方式
r=range(2,12,2)#指定开始，结束，步长
print(list(r))
#判断指定的整数是否在r序列之中in， not in
print(10 in r)
print(10 not in r)