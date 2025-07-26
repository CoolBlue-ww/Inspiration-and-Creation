# 用for循环输出一个菱形
# 菱形上半部分的高度
n = int(input("输入菱形上半部分的行数："))
for i in range(n):
    print(' ' * (n - 1 - i) + "*" * (2 * i + 1))
for i in range(n-1):
    print(' ' * (i + 1) + "*" * (2 * (n - i -2) + 1))
