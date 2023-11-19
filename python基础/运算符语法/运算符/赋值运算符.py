#执行顺序从右到左
from re import L


q=3+4
print(q)
#支持链式赋值
a=b=c=20
print(a,id(a))
print(b,id(b))
print(c,id(c))
#支持参数赋值
x=20
x+=30#相当于x=x+30
x-=10
x*=2
print(x,type(x))
x/=20
print(x,type(x))
x//=3
print(x,type(x))
x%=3
print(x,type(x))
#支持系列解包赋值
a,b,c=20,30,40
print(a,b,c)#交换之前
a,b,c=b,c,a
print(a,b,c)#交换之后