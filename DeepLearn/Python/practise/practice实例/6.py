# 计算圆的面积
# 输入圆的半径
import math

r = float(input("请输入圆的半径："))
# 根据圆的面积公式计算圆的面积
S = math.pi * r**2
# 输出结果
print(f'半径为{r}的圆的面积是{S}')
