from cffi import FFI as affi

ffi = affi()

ffi.cdef(
    """
    int hi();
"""
)

lib = ffi.dlopen("/home/SayMyName/桌面/LEARN/PyThonSO/hello.so")

lib.hi()


