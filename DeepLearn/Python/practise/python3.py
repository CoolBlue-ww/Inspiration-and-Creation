# 14.将一个正整数因式分解
def prime_y(n):
    prime_y_sequence = []
    i = 2
    while i*i <= n:
        if n % i == 0:
            prime_y_sequence.append(i)
            n //= i
        else:
            i += 1

    if n > 1:
        prime_y_sequence.append(n)
    return prime_y_sequence


n = int(input("请输入一个正整数："))
prime_y_counts = prime_y(n)
print(f"将这个正整数因式分解：{prime_y_counts}")



