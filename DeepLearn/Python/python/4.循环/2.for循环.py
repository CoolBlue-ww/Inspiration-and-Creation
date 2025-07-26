result = 0
n = 3
for i in range(n+1):
    if i > 0:
        factorial = 1
        for j in range(i + 1):
            if j > 0:
                factorial *= j
        result += factorial
print(result)


result = 0
n = 3
i = 1
while i <= n:
    factorial = 1
    j = 1
    while j <= i:
        factorial *= j
        j += 1
    i += 1
    result += factorial
print(result)
