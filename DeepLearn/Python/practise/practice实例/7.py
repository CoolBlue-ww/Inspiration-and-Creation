# 生成随机数
import random

num1 = random.randint(1, 10000)  # 1到10000内包含端点的随机整数
num2 = random.random()  # 随机选出介于0到1之间的小数

list = [1, 2, 3, 4, 5, 6, 7]
num3 = random.choice(list)  # 从列表中随机选出一个值，所有项的概率相同
num4 = random.choices(list, weights=[1, 1, 1, 1, 1, 1, 10], k=3)  # 随机从列表中挑选k项，weights可以修改对应项的抽取概率

list2 = [2, 4, 6, 3, 6, 7]
random.shuffle(list2)  # 将原列表顺序打乱，打乱后不需要对其赋值，因为是在列表中原地打乱

print(num1, num2, num3, num4, list2)
