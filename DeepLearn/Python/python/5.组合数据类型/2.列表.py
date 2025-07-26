a = 1
b = '('
c = '@'
d = 'hello'

# 只能转化字符串
list1 = list('abcdefg')
print(list1)
result = ''.join(list1)  # 合并列表字符串
print(result)

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'hello', "10", 3.6, True]

# 向列表里面增加内容
list_1.append(12)
print(list_1)

list_1.extend()