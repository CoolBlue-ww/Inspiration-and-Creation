# 计算三角形的面积
# 判断用户输入的内容是否合法
def get_float_input(n):
    while True:
        try:
            return float(input(n))
        except ValueError as e:
            print(f"输入的内容无效：{e}")

import math
# 封装函数计算三角形的面积
def compute_area(a, b, c):
    # 三角形的半周长
    l = (a + b + c) / 2
    # 根据海伦公式求解三角形面积
    area = math.sqrt(l * (l - a) * (l - b) * (l - c))
    return area


# 建立一个主函数
def main():
    # 输入三边a,b,c的值
    a = get_float_input("请输入a边的值：")
    b = get_float_input("请输入b边的值：")
    c = get_float_input("请输入c边的值：")
    # 检查三边长度的取值是否符合数学逻辑
    while (a + b) <= c or (a + c) <= b or (b + c) <= a:
        print("输入的边长不符合数学逻辑请重新输入！")
        a = get_float_input("请重新输入a边的值：")
        b = get_float_input("请重新输入b边的值：")
        c = get_float_input("请重新输入c边的值：")
    # 计算三角形的面积
    area = compute_area(a, b, c)
    # 打印计算结果
    print(f'这个三角形的面积为：{area}')


# 程序入口
if __name__ == "__main__":
    main()
