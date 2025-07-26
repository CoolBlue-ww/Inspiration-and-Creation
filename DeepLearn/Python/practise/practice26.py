# 利用递归求5！
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


# 定义n的值
n = 5
result = factorial(n)
print(result)