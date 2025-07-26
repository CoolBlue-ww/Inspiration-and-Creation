import math
num = int(input('请输入一个整数：'))
if num <= 1:
    print(f'这个数{num}不是质数！')
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f'这个数{num}为质数！')
    else:
        print(f'这个数{num}为合数！')

