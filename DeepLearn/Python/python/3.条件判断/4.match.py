# # match(常量匹配)
# name = input('请输入文字：')
# match name:
#     case '小狗':
#         print('这是一只小狗')
#     case '小猫':
#         print('这是一只小猫')
#     case _:
#         print('不知道这是啥？')


age = input('请输入你的年龄：')
if age.isdigit():
    age = int(age)
    if age > 0 and age < 120:
        print('年龄输入正确！')
    else:
        print('年龄输入错误！请重新输入！')
        age = int(input('你的年龄是：'))
        if age > 0 and age < 120:
            print('年龄输入正确！')
        else:
            print('又输入错误了！')
else:
    print('请输入阿拉伯数字！')
    age = int(input('你的年龄是：'))
    if age > 0 and age < 120:
        print('年龄输入正确！')
    else:
        print('年龄输入错误！请重新输入！')
        age = int(input('你的年龄是：'))
        if age > 0 and age < 120:
            print('年龄输入正确！')
        else:
            print('又输入错误了！')