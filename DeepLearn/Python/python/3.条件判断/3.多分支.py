# age = int(input('请输入你的年龄：'))
# if age > 18:
#     print('你已经成年了！')
# elif age == 18:
#     print('你刚好成年！')
# else:
#     print('你还未成年！')


age = int(input('请输入你的年龄：'))
if age >= 18:
    print('你已经成年了！')
# 嵌套选择
else:
    if 16 < age < 18:
        total = 18 - age
        print('你距离成年还有%d年！' % total)
    else:
        print('你距离成年还有很久！')


bmi = (float(input('请输入你的体重（斤）：')) / 2) / (float(input('请输入你的身高（cm）：')) / 100)**2
if bmi < 18.5:
    print('你简直就是只细狗！')
elif bmi < 23.9:
    print('完美身材！')
else:
    print('小胖纸')
