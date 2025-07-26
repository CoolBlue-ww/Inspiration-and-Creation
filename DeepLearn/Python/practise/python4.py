# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
grade = float(input("请输入您的成绩："))
grade = 'A' if grade >= 90 else 'B' if grade >= 60 else 'C'

