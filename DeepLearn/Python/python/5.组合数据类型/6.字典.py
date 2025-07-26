a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
c = 1
b = dict(a=3, b=4, c=5)
# 增加
b['d'] = '+='
print(b)
r = b['d']
print(r)
# 修改键值对
b['c'] = 6
print(b)
