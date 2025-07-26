# 识别字符串中的英文字母，空格，数字，以及其他符号的个数。
def count_characters():
    # 输入一串字符串
    input_string = input("输入一串字符")

    # 初始化列表
    count_letter = 0
    count_space = 0
    count_digit = 0
    count_other = 0

    for char in input_string:
        if char.isalpha():
            count_letter += 1
        elif char.isspace():
            count_space += 1
        elif char.isdigit():
            count_digit += 1
        else:
            count_other += 1

    print(f"英文字母个数：{count_letter}")
    print(f"空格个数：{count_space}")
    print(f"数字个数：{count_digit}")
    print(f"其他字符：{count_other}")


count_characters()
