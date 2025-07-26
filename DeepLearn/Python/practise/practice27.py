# 利用递归函数调用将输入的五个字符按相反的顺序打印出来
def reverse_print(s, index):
    if index < 0:
        return
    print(s[index], end='')
    reverse_print(s, index - 1)


if __name__ == '__main__':
    input_string = input("请输入五个字符：")
    if len(input_string) != 5:
        print('你输入的字符数目不对！')
    else:
        reverse_print(input_string, len(input_string) - 1)