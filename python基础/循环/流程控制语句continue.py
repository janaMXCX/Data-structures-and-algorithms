#输出1到50之间所有5的倍数
#五的倍数的共同点，和5的余数为0的数就是五的倍数
#反过来理解什么样的数不是5的倍数
for a in range(1,51):
    if a%5==0:
        print(a,"为5的倍数")
#使用continue时完成上述方案
for b in range(1,51):
    if b%5!=0:
        continue
    print(b)

#break和continue只控制本层语句
for i in range(5):
    for j in range(11):
        if j%2==0:
            continue
        print(j,end="\t")
    print()