"""
upper()
lower()
"""
s='hello,python'
a=s.upper()
print(a,id(a))#会产生新的字符串类型
print(s,id(s))
b=s.lower()#会产生新的字符串类型
print(b,id(b))
print(s,id(s))


s2='hello,Python'
print(s2.swapcase())
print(s2.title)#把每个单词的第一个字符转化为大写，把其他的部分转化为小写
