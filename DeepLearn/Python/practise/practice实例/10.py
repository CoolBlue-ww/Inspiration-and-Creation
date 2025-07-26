"""
通过使用 if...elif...else 语句判断数字是正数、负数或零
"""
# 输入一个数字
number = float(input("请输入一个整数或浮点数："))
# 对输入的数字进行条件判断
if number > 0:
    print("这是一个正数")
elif number < 0:
    print("这是一个负数")
else:
    print("这个数为零")
