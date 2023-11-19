#将其他数据类型转化为float类型
a=20
b=2.3
c="234"
d="hello"
e="1.23"
f=True
print(type(a),type(b),type(c),type(d),type(e),type(f))
print(float(a),type(float(a)))
print(float(b),type(float(b)))
print(float(c),type(float(c)))
#print(float(d),type(float(d)))  这句话会报错如果字符串中的数据为非数字串，则不允许转换
print(float(e),type(float(e)))
print(float(f),type(float(f)))
#转化时整数会在后面加一位小数