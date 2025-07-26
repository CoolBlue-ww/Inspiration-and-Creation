# 像列表一样跨步
for i in range(1, 10, 2):
    print(i)

# 三种方法做水仙花数
for i in range(1000):
    a = i // 100
    b = i % 100 // 10
    c = i % 10
    if a**3 + b**3 + c**3 == i:
        print(i)
print('*'*100)
for i in range(100, 1000):
    str_num = str(i)
    a = int(str_num[0])
    b = int(str_num[1])
    c = int(str_num[2])
    if a**3 + b**3 + c**3 == i:
        print(i)
print('~'*100)
for i in range(1, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            if i**3 + j**3 + k**3 == (i*100) + (j*10) + (k):
                print('%d%d%d' % (i, j, k))
