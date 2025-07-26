from cffi import FFI as C
import time


def compte(a, b):
    num = a + b
    return num



ffi = C()
ffi.cdef(
    """
    int compte(int a, int b);
"""
)

db = ffi.dlopen("/home/SayMyName/桌面/GitHub/MyCode/C/PyThonSO/test.so")

t1 = time.time()
num = db.compte(1000000000, 1000000000)
t2 = time.time()
print(t2 - t1)

t3 = time.time()
num = compte(1000000000, 1000000000)
t4 = time.time()
print(t4 - t3)

if (t4 - t3) > (t2 - t1):
    print("Yes")
else:
    print("No")