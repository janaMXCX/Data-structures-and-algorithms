s='hello,python'
s1=s[:5]#从0开始切到5
s2=s[6:]#从6开始切到最后
s3='!'
newstr=s1+s2+s3

print(s1)
print(s2)
print(newstr)

print(id(s))
print(id(s1))
print(id(s2))
print(id(s3))
print(id(newstr))


print('------------切片[start:end:step]------------')
print(s[1:5:1])#从一开始截到5，不包括5，步长为1
print(s[::2])
print(s[::-1])#默认从字符串最后一个元素开始，到第一个元素结束
