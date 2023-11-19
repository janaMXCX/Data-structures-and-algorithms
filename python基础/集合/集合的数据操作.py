#集合的数学操作
#(1)交集
s1={10,20,30,40}
s2={20,30,40,50,60}
print(s1.intersection(s2))
print(s1 & s2)
print(s1)
print(s2)
#(2)并集
print(s1.union(s2))
print(s1| s2)
print(s1)
print(s2)
#(3)差值操作
print(s1.difference(s2))
print(s1-s2)
print(s1)
print(s2)
#(4)对称差值
print(s1.symmetric_difference(s2))
print(s1^s2)