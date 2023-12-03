
lis = [1, 2, 3, 4]

lis.append(10)  # 列表的尾部插入
print(lis)
lis.insert(1, 20)  # 在索引为1的位置上插入
print(lis)
lis.remove(3)  # 删除
print(lis)
lis[4] = 30  # 替换
print(lis)
c = lis.pop()
print(c)


i = lis.index(20)  # 查找
print(i)