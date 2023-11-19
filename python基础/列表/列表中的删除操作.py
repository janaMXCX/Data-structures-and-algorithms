#remove()一次删除一个元素，重复元素只删除第一个，元素不存在抛出Value error
lst=[10,20,30,40,50,60,30]
lst.remove(30)
print(lst)
#pop()删除一个指定索引位置上的元素，指定索引不存在抛出IndexEError，不指定索引元素删除列表中最后一个元素
lst.pop(1)
print(lst)
lst.pop()#不指定参数删除最后一个
print(lst)
#切片 一次至少删除一个元素，将产生一个新的列表对象
lst2=lst[1:3]#删除索引1到索引3的内容但是不包括索引3
print(lst)
print(lst2)
#不产生新的对象，而是删除原来列表中的内容
lst[1:3]=[]
print(lst)
#clear()清空列表del()删除列表