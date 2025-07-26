# 阶乘factorial是所有小于及等于该数的正整数的积
num = int(input('请输入一个正整数：'))
if num < 0:
    print('负数没有阶乘！')
elif num == 0:
    print('0的阶乘为1!')
else:
    factorial = 1
    n = 1
    while n <= num:
        factorial *= n
        n += 1
    print(f'正整数{num}的阶乘为{factorial}。')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

num = int(input('请输入一个正整数：'))
if num < 0:
    print('负数没有阶乘！')
elif num == 0:
    print('0的阶乘为1!')
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f'正整数{num}的阶乘为{factorial}.')
