year = int(input('请输入一个年份：'))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('这个年份是润年！')
else:
    print('这个年份不是闰年！')