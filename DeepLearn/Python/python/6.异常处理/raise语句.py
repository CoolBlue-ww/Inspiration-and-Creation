try:
    num = int(input('请输入大于8的数字：'))
    if num < 8:
        raise Exception("输入有误")
except Exception as e:
    print(e)
