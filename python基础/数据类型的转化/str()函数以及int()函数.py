name="张三"
age=20
print(type(name),type(age))#name和age的数据类型不相同
print('我叫'+name+'今年'+str(age)+'岁')#这个是对的
print('我叫'+name+'今年'+age+'岁')#这个是错的
#str将其他的数据类型转化成字符串str(123)
a=20
b=2.5
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))
#int将其他类型转化为int类型，整数类型
s2='1221'#如果将字符串转化为int整数类型，字符串必须为 数字串 不可以是小数串
f1=True#转化为int整数类型时会转化为0或者1
s1=2.3#浮点类型转化为int整数类型时，只截取整数部分。
print(int(s1),type(int(s1)))
print(int(f1),type(int(f1)))
print(int(s2),type(int(s2)))
