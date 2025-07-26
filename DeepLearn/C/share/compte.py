from cffi import FFI as fi
import time
from tqdm import tqdm

ffi = fi()

ffi.cdef(
    """
    int compte(void);
"""
)

lib = ffi.dlopen("/home/SayMyName/桌面/LEARN/PyThonSO/compte.so")

start_time = time.time()

result = lib.compte()

end_time = time.time()

print(f"利用C语言通过for循环计算1到100累加的和为：{result}，累积用时：{end_time - start_time}秒。")


total = 0
start_timr = time.time()
for i in range(1, 1000000001):
    total += i
end_time = time.time()

print(f"利用PyThon语言通过for循环计算1到100000000累加的和为：{total}，累积用时：{end_time - start_time}秒。")

