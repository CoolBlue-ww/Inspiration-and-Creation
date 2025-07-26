"""
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
"""
# 定义数列的第一项
start_number = 2 / 1
# 定义数列的下一项
next_number = 1 + 1 / start_number
# 初始化数列前20项的和S
S = 2
for _ in range(19):
    S += next_number
    next_number = 1 + 1 / next_number
# 输出结果
print('这个数列的前20项的和为：{}'.format(S))

# 答案：32.660263