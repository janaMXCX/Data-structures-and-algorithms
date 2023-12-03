# 读取输入
n = int(input())
students = []

# 读取学生信息并计算总分
for i in range(n):
    scores = list(map(int, input().split()))
    total_score = sum(scores)
    students.append((i + 1, total_score, scores))  # 包括学号、总分、三门成绩


# 按规定排序方式对学生进行排序
students.sort(key=lambda x: (-x[1], -x[2][0], -x[2][1], -x[2][2], x[0]))

# 输出前五名学生的学号和总分
for i in range(min(5, n)):
    student_id, total_score = students[i][0], students[i][1]
    print(f"{student_id} {total_score}")
