from cffi import FFI as C
import time

ffi = C()

lib1 = ffi.dlopen("/home/SayMyName/桌面/GitHub/MyCode/C/PyThonSO/daffodil_num.so")
lib2 = ffi.dlopen("/home/SayMyName/桌面/GitHub/MyCode/C/PyThonSO/daffpdil_num_2.so")
ffi.cdef(
    """void print_num(void);"""
)

start_time1 = time.time()
lib1.print_num()
end_time1 = time.time()
sub1 = end_time1 - start_time1

print("-" * 50)

start_time2 = time.time()
lib2.print_num()
end_time2 = time.time()
sub2 = end_time2 - start_time2

if sub1 > sub2:
    print(f"单层循环比多层循环快：{sub1 - sub2}")
else:
    print(f"多层循环比单层循环快: {sub2 - sub1}")

# 循环嵌套少的略快

# 153
# 370
# 371
# 407 

