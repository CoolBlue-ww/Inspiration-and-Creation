"""
一球从100米高度自由落下，每次落地后反跳回原高度的一半；
再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
"""

height = 100
total_distance = height  # 初始下落100米
current_height = height / 2  # 第一次反弹后的高度

# 循环计算第1次到第9次反弹后的下落和上升路程
for _ in range(9):
    total_distance += 2 * current_height  # 每次反弹后的下落和上升总和
    current_height /= 2

# 第十次反弹的高度
tenth_rebound = current_height

# 输出结果
print("第十次落地时，总共经过的距离为：{} 米".format(total_distance))
print("第十次反弹的高度为：{} 米".format(tenth_rebound))

# 299.609375   0.09765625
