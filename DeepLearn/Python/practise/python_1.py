def is_prime():
    prime_sequence = []
    for x in range(101, 201):
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                break
        else:
            prime_sequence.append(x)
    return prime_sequence


prime_counts = is_prime()
print("输出结果")
print(f"这个范围内的素数：{prime_counts}")
