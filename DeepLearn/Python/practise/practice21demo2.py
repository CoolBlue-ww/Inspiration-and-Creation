peach_number = 1
current_peach_number = (peach_number + 1) * 2
for _ in range(8):
    last_peach_number = (current_peach_number + 1) * 2
    current_peach_number = last_peach_number
print(last_peach_number)

# 答案：1534