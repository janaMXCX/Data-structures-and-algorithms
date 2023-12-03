"""
逆波兰表达式
"""
from sstak import *

st = SStack()

while True:
    exp = input()
    tmp = exp.split(" ")  # split 按空格切割 生成的结果是一个列表

    print(tmp)

    for i in tmp:
        if i not in ["+", "-", "*", "/", "p"]:
            st.push(float(i))
        elif i == "+":
            y = st.pop()
            x = st.pop()
            st.push(x + y)
        elif i == "-":
            y = st.pop()
            x = st.pop()
            st.push(x - y)
        elif i == "*":
            y = st.pop()
            x = st.pop()
            st.push(x * y)
        elif i == "/":
            y = st.pop()
            x = st.pop()
            st.push(x / y)
        elif i == "p":
            print(st.top())




