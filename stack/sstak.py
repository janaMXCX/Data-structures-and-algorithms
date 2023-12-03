"""
 sstak.py 栈模型的顺序存储
 重点代码

 思路总结：
 1. 列表即顺序存储，单功能多，不符合栈的模型特征
 2. 利用列表 将其封装， 提供接口方式
"""

# 自定义异常
class StackError(Exception):
    pass

# 顺序栈类
class SStack:
    def __init__(self):
        # 空列表就是栈的存储空间
        # 列表的最后一个元素作为栈顶
        self._elem = []

    # 判断是否为空栈，列表是否为空
    def is_empty(self):
        return self._elem == []

    # 查看栈顶元素
    def top(self):
        if self.is_empty():
            raise StackError("Stack is empty")
        return self._elem[-1]

    # 入栈操作
    def push(self, val):
        self._elem.append(val)

    # 出栈操作
    def pop(self):
        if self.is_empty():
            raise StackError("Stack is empty")
        # 弹出并返回
        return self._elem.pop()

    # 取栈长
    def size(self):
        return len(self._elem)


if __name__ == "__main__":
    st = SStack()  # 初始化栈

























