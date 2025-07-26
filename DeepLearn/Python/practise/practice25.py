# 求1+2！+3！+4！+5！····+20！=？
# 初始化数值的和total
total = 0
current_factorial = 1
for n in range(1,21):
    current_factorial *= n
    total += current_factorial
# 输出结果
print(f'这几个数相加的结果是：{total}')