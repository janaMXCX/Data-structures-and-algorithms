a=3.14159
print(a,type(a))
#浮点数的计算不可以直接进行计算，浮点数直接计算有误差，是因为电脑储存类型有错误
#例如以下计算
n1=2.2
n2=1.1
n3=2.1
print(n1+n2)#个别的浮点类型数字相加会出现错误。
print(n1+n3)
from decimal import Decimal
print(Decimal("1.1")+Decimal("2.2"))