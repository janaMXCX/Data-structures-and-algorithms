"""
linklist.py
功能 ： 实现单链表的构建和功能操作
"""

# 创建节点类
class Node:
    """
    将自定义的类是为节点的生成类，实例对象中
    包含数据部分和指向下一个节点的 next
    """
    def __init__(self, val, next=None):
        self.val = val  # 存储有用的数据
        self.next = next  # 循环下一个节点关系
class LinkList:
    """
    思路： 单链表类，生成对象之后可以进行增删改查操作
          集体操作通过调用具体方法完成
    """
    def __init__(self):
        """
        初始化链表，标记一个链表的开端，以便于获取后续的节点
        """
        self.head = Node(None)

    # 通过list_为链表添加一组节点
    def init_list(self, list_):
        p = self.head  # p作为移动变量
        for item in list_:
            p.next = Node(item)
            p = p.next
    # 遍历链表
    def show(self):
        p = self.head.next  # 第一个有效节点
        while p is not None:
            print(p.val)
            p = p.next  # p 向后移动

    # 获取链表长度
    def length(self):
        p = self.head.next
        length = 0
        while p is not None:
            length += 1
            p = p.next
        return length

    # 判断链表为空
    def is_empty(self):
        if self.head.next is None:
            return True
        else:
            return False

    # 清空链表
    def clear(self):
        self.head.next = None

    # 尾部插入
    def append(self, val):
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(val)

    # 头部插入
    def head_insert(self, val):
        node = Node(val)
        node.next = self.head.next
        self.head.next = node

    # 指定插入位置
    def insert(self, index, val):
        # 此处的index为指定的位置
        p = self.head
        for i in range(index):
            # 超出最大范围结束循环
            if p.next is None:
                break
            p = p.next

        node = Node(val)
        node.next = p.next
        p.next = node

    # 删除节点按值删除
    def delete(self, x):
        p = self.head
        # 结束循环 必然两个条件其一为假
        # and短路原则
        while p.next and p.next.val != x:
            p = p.next

        if p.next is None:
            raise ValueError("没有找到该值")
        else:
            p.next = p.next.next

    # 获取某一个节点的值
    # 传入节点的位置获取节点的值
    def get_index(self, index):
        if index < 0:
            raise IndexError("索引不能为负数")
        p = self.head.next
        for i in range(index):
            if p.next is None:
                raise IndexError("没有获取到这个位置的值")
            p = p.next
        return p.val

    # 修改某一个索引为位置的值
    # 注意这里的索引是从0开始的
    def revise(self, index, x):
        if index < 0:
            raise IndexError("索引不能为负数")
        p = self.head.next
        for i in range(index):
            if p.next is None:
                raise IndexError("没有获取到这个位置的值")
            p = p.next
        p.val = x

