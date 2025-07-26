# while True:
#     password = input('请输入密码:')
#     if password == '123456789':
#         print('密码正确！')
#         break
#     else:
#         print('密码错误！')
#
# n = 10
# for i in range(n):
#     if i > 0:
#         if n % i != 0:
#             print(i)
#             break


# n = 4
# m = 2
# k = 0
# while m < n:
#     if n % m == 0:
#         # print('这个数不是质数')
#         k = 1  # 标志变量
#         break
# # else:
# #     print('这个数是质数！')
# if k == 1:
#     print('这个数不是质数！')

n = 11
m = 2
while m < n:
    if n % m == 0:
        print('n不是质数')
        break
    m += 1
else:
    print('这个数是质数！')