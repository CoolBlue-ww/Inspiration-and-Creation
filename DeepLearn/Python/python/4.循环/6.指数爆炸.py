import sys
sys.set_int_max_str_digits(10000)

# 折纸
n = 0.5
for _ in range(50):
    n *= n
    print(n)


# 国王数麦子
maili = 1
gezi = 1
total = 0
while gezi <= 100:
    total += maili
    gezi += 1
    maili *= 2
print(total)


# 人生复利
day = 1
total = 0
while day <= 365:
    total += 0.1
    day += 1
print(total)
