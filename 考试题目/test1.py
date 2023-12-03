#
# def find_base(p, q, r):
#     for base in range(2, 17):
#         try:
#             p_base = int(str(p), base)
#             q_base = int(str(q), base)
#             r_base = int(str(r), base)
#
#             if p_base * q_base == r_base:
#                 return base
#         except ValueError:
#             # 忽略在基数转换中出现的 ValueError
#             pass
#
#     return 0
#
#
# # 输入三个整数 p, q, r
# p, q, r = int(input("输入 p: ")), int(input("输入 q: ")), int(input("输入 r: "))
#
# result = find_base(p, q, r)
#
# if result != 0:
#     print(result)
# else:
#     print("无合适的进制")
#
#
#
# def find_base(p, q, r):
#     for base in range(2, 17):
#         p_base = convert_base(p, base)
#         q_base = convert_base(q, base)
#         r_base = convert_base(r, base)
#
#         if p_base * q_base == r_base:
#             return base
#     return 0
#
# def convert_base(num, base):
#     result = 0
#     multiplier = 1
#     while num > 0:
#         remainder = num % base
#         result += remainder * multiplier
#         multiplier *= 10  # Move to the next decimal place
#         num //= base
#     return result
#
# # 输入三个整数 p, q, r
# p, q, r = int(input("输入 p: ")), int(input("输入 q: ")), int(input("输入 r: "))
#
# result = find_base(p, q, r)
#
# if result != 0:
#     print(f"最小进制为: {result}")
# else:
#     print("无合适的进制")
#





def b2ten(num, base):
    ret = 0
    cnt = 0
    digit = []

    while num != 0:
        digit.append(num % 10)
        num = num // 10

    cnt = len(digit) - 1

    while cnt >= 0:
        if digit[cnt] >= base:
            return -1  # 数字超过B进制的数码范围
        ret = ret * base + digit[cnt]
        cnt -= 1

    return ret


def find_base(p, q, r):
    for b in range(2, 17):
        pb = b2ten(p, b)
        qb = b2ten(q, b)
        rb = b2ten(r, b)

        if pb == -1 or qb == -1 or rb == -1:
            continue

        if pb * qb == rb:
            return b

    return 0


# 输入三个整数 p, q, r
p, q, r = map(int, input("输入 p, q, r: ").split())

result = find_base(p, q, r)

if result != 0:
    print(result)
else:
    print("无合适的进制")
