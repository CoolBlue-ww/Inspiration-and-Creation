# 13.找出水仙花数
for x in range(1, 10):
    for y in range(0, 10):
        for z in range(0, 10):
            if x**3 + y**3 + z**3 == (x*100 + y*10 + z):
                print("%d%d%d" % (x, y, z))
