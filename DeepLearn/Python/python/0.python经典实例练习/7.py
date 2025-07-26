# 导入random库来抽取随机数
import random
a = random.randint(1, 5)
b = random.random()
c = random.uniform(1.5, 2.5)
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = random.choice(list)
e = random.choices(list, k=3)
random.shuffle(list)
print(a, b, c, d, e, list)
