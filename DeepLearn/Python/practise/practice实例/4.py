# 求解一个二元一次方程
"""
封装一个函数用来检测用户输入的值是否是浮点数，
如果不是提交错误信息并重新输入。
"""

import cmath


def get_float_input(n):
    while True:
        try:
            return float(input(n))
        except ValueError as e:
            print(f'此输入无效：{e}')


"""
封装一个函数根据求根公式来计算方程的根
"""


def solve_equation(a, b, c):
    # 先求出根的判别式d
    d = b ** 2 - 4 * a * c
    # 利用求根公式计算方程的根
    root1 = (-b + cmath.sqrt(d)) / (2 * a)
    root2 = (-b - cmath.sqrt(d)) / (2 * a)
    # 返回计算结果
    return root1, root2


"""
建立一个主程序
"""


def main():
    print("计算a*x**2 + b*x + c")
    # 输入参数的值并且保证a不能为0
    a = get_float_input("请输入参数a的值（a不能为0）：")
    while a == 0:
        print("a的值不能为0!")
        a = get_float_input("请重新输入a的值：")
    b = get_float_input("请输入一次项系数b的值：")
    c = get_float_input("请输入常数项c的值：")
    # 调用主要的计算函数来计算方程的根
    root1, root2 = solve_equation(a, b, c)
    # 输出结果
    print(f"方程的根分别为：{root1}, {root2}")


# 设置程序的入口
if __name__ == '__main__':
    main()
