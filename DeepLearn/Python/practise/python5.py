# 求两个正整数的最大公因数和最小公倍数

import math
# 定义两个正整数
a = int(input("请输入第一个正整数："))
b = int(input("请输入第二个正整数："))

GCD = math.gcd(a, b)
LCM = abs(a * b) // GCD

print(f"这两个数的最小公倍数和最大公约数：{GCD}, {LCM}")
