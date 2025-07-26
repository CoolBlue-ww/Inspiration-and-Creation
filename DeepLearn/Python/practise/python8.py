# 求一千以内的完数
def proper_divisors(n):
    # 初始化列表
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

for n in range(1, 1001):
    result = proper_divisors(n)
    proper_divisors_sum = sum(result)
    if proper_divisors_sum == n and n != 1:
        print(f"一千以内的完数：{n}")
