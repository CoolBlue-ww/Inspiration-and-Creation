# 初始化高度
height = 100
# 当前高度
current_height = height / 2
# 初始化一个列表用来储存一段小球走过的路程
distance_list = []
for _ in range(9):
    distance_list.append(current_height)
    current_height = current_height / 2
# 小球第十次下落走过的总路程
total_distance = sum(distance_list) * 2 + 100
# 小球第十次弹起的高度
last_height = height / 2 ** 10
# 输出结果
print("小球的总路程和最后的弹起高度分别为：{}, {}".format(total_distance, last_height))

# 299.609375  0.09765625
