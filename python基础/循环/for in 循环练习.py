#输出100到999之间的水仙花数
#利用for in 函数
for a in range(100,1000,1):
    x=a%10
    y=a//10%10
    z=a//100
    if x**3+y**3+z**3==a:
        print(a,"为水仙花数")