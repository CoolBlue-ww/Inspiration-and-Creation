# # 转化为整数int
# # 字符串转化为整数
# s = '12345'
# print(int(s))
# print(s)
# # 浮点数可以转化为整数
#
# # 布尔bool也可以转化成整数
# s2, s3 = True, False
# print(int(s2), int(s3))
#
#
# # 转化为浮点数float
# # 字符串转化为浮点数
# print(float(s))
# # int转float
# n = 4
# print(float(n))
# # bool-->float
# print(float(s2), float(s3))
#
# # 转化为bool
# # str-->bool
# s1 = ' '
# print(bool(s1))  # 有内容就是true
# # int-->bool
# m = 1
# print(bool(m))
# # float-->bool
# k = 0
# print(bool(k))

# 转化为字符串
n = 5
print(type(str(n)))
m = 9.3
print(type(str(m)))
s1 = True
s2 = False
print(type(str(s1)), type(str(s2)))



# int进制的转换
s = '10'
print(int(s, 2))
