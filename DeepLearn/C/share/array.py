import numpy as np
import time
from cffi import FFI as C
from tqdm import tqdm


def array():
    # 定义循环从次数
    num = 1000000000
    # 定义一个初始化数组
    total_array = np.array([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ])
    for i in tqdm(range(num), desc="numpy数组计算中..."):
        if i <= num / 2:
            total_array += np.array([
                [4, 4, 4],
                [4, 4, 4],
                [4, 4, 4]
            ])
        elif i > (num / 2) and i <= (4 / 5 * num):
            total_array *= np.array([
                [1, 2, 4],
                [4, 2, 1],
                [2, 4, 1]
            ])
        else:
            total_array -= np.array([
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]
            ])
    return 0

start_time = time.time()
result1 = array()
end_time = time.time()
len_time1 = end_time - start_time


ffi = C()
ffi.cdef(
    """
    int array(void);
"""
)
lib = ffi.dlopen("/home/SayMyName/桌面/LEARN/PyThonSO/array.so")

start_time = time.time()
result2 = lib.array()
end_time = time.time()
len_time2 = end_time - start_time

print(f"numpy数组完成计算，累积用时：{len_time1}秒。\nC语言共享库完成计算，累积用时：{len_time2}秒。\n")

