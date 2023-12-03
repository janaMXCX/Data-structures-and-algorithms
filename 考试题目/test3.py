# 传入的形参是一个列表 命名为nums
# result 为一个空的列表
def permute(nums):
    result = []
    generate_permutation(nums, 0, result)
    return result
    # 传出的数据就是之创建好的空列表里面加入的数据


def generate_permutation(nums, index, result):
    if index == len(nums):  # 如果当前 index 等于 nums 长度，说明已经完成一种排列
        result.append(nums.copy())  # 将当前排列的副本添加到结果列表中
        return  # 返回上一级递归

    for i in range(index, len(nums)):  # 对于当前位置 index 开始的所有数字
        nums[index], nums[i] = nums[i], nums[index]  # 将当前位置与后面的位置依次交换，尝试不同的排列
        generate_permutation(nums, index + 1, result)  # 递归调用，继续生成下一个位置的排列
        nums[index], nums[i] = nums[i], nums[index]  # 恢复原始状态，用于下一次交换


def print_permutations(n):
    nums = list(range(1, n + 1))  # 这里创建的是一个列表 nums = [1, 2, 3]
    permutations = permute(nums)

    for p in permutations:
        print(*p, sep='    ')


# 读取输入
n = int(input())

# 输出排列
print_permutations(n)
