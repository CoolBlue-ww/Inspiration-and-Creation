# and, not, or
print(2 and 4)  # 短路运算
print(1 ==1 and True and 9>1)
print('hello' and ' ')
print(0 and 3)
# 二元运算符

print(1 or 3)  # 短路运算
print(True or False)


print(not True)  # 一元运算符取反

# 一元运算符优先级高于二元运算符
print(True and True and not False)

# not > and >or
print(True or False and False or True)