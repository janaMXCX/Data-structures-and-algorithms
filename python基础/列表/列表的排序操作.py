lst=[20,40,98,50,54]
print(lst)
lst.sort()
print(lst)#在原列表进行排序

lst.sort(reverse=True)#降序排序
print(lst)
lst.sort(reverse=False)#降序排序
print(lst)
#内置函数排序
new_lst=sorted(lst)#会产生新的列表对象
print(lst)
print(new_lst)
#指定关键字参数进行列表降序排序
desc_lst=sorted(lst,reverse=True)
print(desc_lst)