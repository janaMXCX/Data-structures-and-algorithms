print('apple'>'app')#Ture
print('apple'>'banana')#False
print(ord('a'),ord('b'))
print(ord('杨'))

print(chr(97),chr(98))
print(chr(26472))

'''==与is的区别
==比较的是value
is 比较的是id是否相等'''
a=b='python'
c='python'
print(a==b)#Ture
print(b==c)#Ture

print(a is b)#Ture
print(a is c)#Ture
print(id(a),id(b),id(c))
