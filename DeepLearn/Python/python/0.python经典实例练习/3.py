import math
num = float(input('请输入一个正数：'))
if num < 0:
    print('在实数范围内，负数无平方根！')
    print('其相反数的平方根为：%.2f' % (-num)**0.5)
else:
    print('这个正数的平方根为： %.2f' % math.sqrt(num))
