"""
交换变量
"""
x = float(input("请输入变量x的值："))
y = float(input("请输入变量y的值："))
# 交换变量
temp = x
x = y
y = temp
# 打印交换后的x和y
print(f"变量x的值为：{x},变量y的值为：{y}")