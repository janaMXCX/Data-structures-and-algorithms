a={"张三":100,'李四':98,'王五':45}
for i in a:
    print(i)#此时只会获取键
    print(i,a[i],a.get(i))
#字典的键不可以重复值可以重复。
#字典中的元素是无序的。
#字典也可以根据需要，动态地进行伸缩
#键必须是不可变对象，不可以为列表。
#字典会浪费较大的内存