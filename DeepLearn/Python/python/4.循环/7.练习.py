# m行n列的矩形

m = 5
n = 5
for i in range(m):
    while True:
        print('*' * n)
        break
    print()


for i in range(m):
    print('*' * n)


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


for i in range(m):
    for j in range(n):
        print('*', end='')
    print()

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

m = n = 5
i = 0
while i < m:
    j = 0
    while j < n:
        print('*', end='')
        j += 1
    print()
    i += 1

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 打印一个有m行的三角形。
m = 20
for j in range(m + 1):
    if j == 0:
        pass
    else:
        print(' ' * (m - j) + (2 * j - 1) * '*')


# 猴子吃桃
day1 = 10
# 剩下来的桃子
day2 = day1 / 2 - 1
# 从最后一天逆推回第一天吃的总桃子。
day1 = (day2 + 1) * 2

# 假如第10天还有1个桃子。
day10 = current_day = 1
for _ in range(9):
    yesterday = (current_day + 1) * 2
    current_day = yesterday
print(f'小猴子第一天一共摘了{current_day}个桃子。')


# 解决猴子吃桃问题的第二种方法——穷举。
peach = 1  # 假设第一天的桃子数为1
while True:
    day1 = peach / 2 - 1
    day2 = day1 / 2 - 1
    day3 = day2 / 2 - 1
    day4 = day3 / 2 - 1
    day5 = day4 / 2 - 1
    day6 = day5 / 2 - 1
    day7 = day6 / 2 - 1
    day8 = day7 / 2 - 1
    day9 = day8 / 2 - 1
    # 第十天发现只有一个桃子，也就是吃到了第9天。
    day10 = day9
    if day10 == 1:
        print(f'小猴子第一天一共摘了{peach}个桃子。')
        break
    else:
        peach += 1


# 9 * 9 的乘法口诀表
# for循环
for i in range(10):
    if i == 0:
        pass
    else:
        for j in range(i + 1):
            if j == 0:
                pass
            else:
                print(f'{i} * {j} = {i * j}', end='\t')
    print()


# while循环
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print('%d * %d = %d' % (i, j, i * j), end='\t')
        j += 1
    print()
    i += 1
