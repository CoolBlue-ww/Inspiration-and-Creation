from cffi import FFI as C
import time


def print_num():
    for x in range(1, 10):
        for y in range(0, 10):
            for z in range(0, 10):
                if x ** 3 + y ** 3 + z ** 3 == x * 100 + y * 10 + z:
                    print("%d%d%d 是水仙花数" % (x, y, z))
    return


ffi = C()
ffi.cdef(
    """
    void print_num(void);
"""
)
lib = ffi.dlopen("/home/SayMyName/桌面/GitHub/MyCode/C/PyThonSO/daffodil_num.so")

start_time1 = time.time()
print_num()
end_time1 = time.time()
sub1 = end_time1 - start_time1
print(f"python打印水仙花数耗时：{sub1}")

start_time2 = time.time()
lib.print_num()
end_time2 = time.time()
sub2 = end_time2 - start_time2
print(f"cffi调用C打印水仙花数耗时： {sub2}")


if sub1 > sub2:
    print(f"Python打印水仙花数比C慢了{sub1 - sub2}")
else:
    print(f"C打印水仙花数比Python慢了{sub2 - sub1}")
