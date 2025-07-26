# 初始化高度
height = 100
# 当前高度
current_height = height / 2
# 初始化路程，从第一次弹起开始统计路程
distance = 100
for _ in range(9):
    distance += current_height * 2
    # 更新当前高度
    current_height /= 2

# 第十次弹起的高度
last_height = height / 2 ** 10
# 输出结果
print(f"总路程：{distance}, 最后弹起高度：{last_height}")

#  294  o.o9765625
