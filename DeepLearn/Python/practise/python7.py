# 求s=a+aa+aaa+aaaa+~~~~~的值
def compute_number(a, n):
    # 初始化列表
    s_list = []
    for i in range(n):
        s_list.append(int(str(a) * (i + 1)))
    return s_list


# 输入数值
a = int(input("输入数值："))
# 输入项数
n = int(input("输入项数："))

result = compute_number(a, n)
s = sum(result)
print(f"这个项数和为：{s}")


