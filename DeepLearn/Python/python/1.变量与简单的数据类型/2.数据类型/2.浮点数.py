# 浮点数运算可能会产生误差
n1 = 14.1
n2 = 4.256
n3 = n1 + n2
print(n3)

n3 = round(n3, 2)  # 保留两位小数
print(n3)

import math
# 向上取整
n4 = math.ceil(n3)
print('向上取整', n4)


n5 = math.floor(n3)
print('向下取整是：', n5)
