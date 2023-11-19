#输出一个三行四列的矩形
"""
for i in range(1,4):  #行表，执行三次一次是一行
    for j in range(1,5):
        print('*',end='\t')
    print()
"""
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"*",j,"=",i*j,end=" ")
    print()