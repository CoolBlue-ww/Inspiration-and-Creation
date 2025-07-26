"""
：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个
 第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下 的一半零一个。
到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
"""
# 从后往前推，初始化桃子的数量
peach_number = 1
# 定义当前的桃子数量
current_peach_number = (peach_number + 1) * 2
for _ in range(8):
    # 更新八次桃子数量的值
    current_peach_number = (current_peach_number + 1) * 2
# 输出结果
print(f"第一天猴子总共摘了：{current_peach_number}个桃")


# 答案：1534