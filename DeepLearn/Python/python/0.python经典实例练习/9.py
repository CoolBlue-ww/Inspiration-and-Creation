# 交换变量
a = input('请输入第一个变量：')
b = input('请输入第二个变量：')
c = a
a = b
b = c
print(f'交换变量后a为{a},b为{b}')

# 不使用临时变量
x = input('请输入第一个变量：')
y = input('请输入第二个变量：')
x, y = y, x
print('变量x为{}'.format(x))
print('变量y为{}'.format(y))
