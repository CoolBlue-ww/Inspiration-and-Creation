import math


def compute_area(a, b, c):
    s = (a + b + c) / 2
    area = s * math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def num():
    a = float(input('请输入第一条边长：'))
    b = float(input('请输入第二条边长：'))
    c = float(input('请输入第三条边长：'))
    if a != 0 and b != 0 and c != 0:
        if (a + b) > c and (a + c) > b and (b + c) > a:
            return a, b, c
        else:
            print('输入的边不符合三角形的数学逻辑，请重新输入！')
            a = float(input('请输入第一条边长：'))
            b = float(input('请输入第二条边长：'))
            c = float(input('请输入第三条边长：'))
            return a, b, c
    else:
        print('三角形的边长不能为零，请重新输入！')
        a = float(input('请输入第一条边长：'))
        b = float(input('请输入第二条边长：'))
        c = float(input('请输入第三条边长：'))
        if (a + b) > c and (a + c) > b and (b + c) > a:
            return a, b, c
        else:
            print('输入的边不符合三角形的数学逻辑，请重新输入！')
            a = float(input('请输入第一条边长：'))
            b = float(input('请输入第二条边长：'))
            c = float(input('请输入第三条边长：'))
            return a, b, c


def main():
    a, b, c = num()
    area = compute_area(a, b, c)
    print(f'边长分别为{a},{b},{c}的三角形的面积为：{area}')


if __name__ == '__main__':
    main()
