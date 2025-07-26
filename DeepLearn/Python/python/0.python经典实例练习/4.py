import cmath  # 导入cmath而非math是为了保证判别式为负数时，方程也有根。


def compute(a, b, c):
    dt = b ** 2 - 4 * a * c
    gen1 = (-b + cmath.sqrt(dt)) / (2 * a)
    gen2 = (-b - cmath.sqrt(dt)) / (2 * a)
    return gen1, gen2


# 输入一元二次方程的三个系数，并封装一个函数来判断输入的系数是否合法。
def jiance_num():
    a = float(input('请输入二次项的系数：'))
    if a == 0:
        print('二次项系数不能为零，请重新输入！')
        a = float(input('请再次输入二次项的系数：'))
    b = float(input('请输入一次项的系数：'))
    c = float(input('请输入常系数：'))
    return a, b, c


def main():
    a, b, c = jiance_num()
    gen1, gen2 = compute(a, b, c)
    print(f'计算方程{a}x**2 + {b}x + {c}')
    print(f'这个一元二次方程的两个根分别为：{gen1}, {gen2}')


if __name__ == '__main__':
    main()
