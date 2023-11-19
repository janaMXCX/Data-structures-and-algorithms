#集合元素的判断操作
#使用in或者not in
s={4,5,8,6,4,2,5}
print(4 in s )
print(100 in s)
print(100 not in s )
print(4 not in s )
'''集合元素的新增操作'''
#调用add()方法，一次添中一个元素
s.add(100)
print(s)
#使用update()方法至少添中一个元素
s.update({200,400,300})
s.update([100,200,300])
s.update((100,200,300))
print(s)
'''集合元素的删除操作'''
#调用remove()方法，一次删除一个指定元素，如果指定的元素不存在抛出KeyError
s.remove(100)
print(s)
#s.remove(500)#KeyError:500
s.discard(500)
print(s)
#调用discard()方法，一次删除一个指定元素，如果指定元素不存在抛出异常
s.discard(500)
print(s)
#调用pop()方法，一次删除一个任意元素
s.pop()
s.pop()
#s.pop(400)#typeError不可以自己加参数
print(s)
#调用clear()方法清空集合
s.clear()
print(s)