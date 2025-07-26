def is_number(x):
    if string.isdigit():
        return True
    else:
        return False


string = input('请输入一串字符串：')
result = is_number(string)
print('这串字符串判断是否为数字的结果为：{}'.format(result))
