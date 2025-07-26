"""
两个乒乓球队进行比赛，各出三人，甲队为 a、b、c 三人，乙队为 x、y、z 三人。
抽签决定比赛名单，有人向队员打听比赛的名单：a 说他不和 x 比，c 说他不和 x、z 比，请编写代码找出三队赛手的名单。
"""
# 定义甲队和乙队各六人
# 甲队
a = 'a'
b = 'b'
c = 'c'
# 乙队
x = 'x'
y = 'y'
z = 'z'
# 初始化一个甲队的对手列表
team = [x, y, z]
for c_opponent in team:
    if c_opponent != x and c_opponent != z:
        print(f"c对{c_opponent}")
        team.remove(c_opponent)
        for a_opponent in team:
            if a_opponent != x:
                print(f"a对{a_opponent}")
                team.remove(a_opponent)
                for b_opponent in team:
                    print(f"b对{b_opponent}")