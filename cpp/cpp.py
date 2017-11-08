
"""
To compile it and run the test, enter:
g++ -std=c++14 -c -fPIC ./cpp/_main.cpp -o ./cpp/CPP.o
g++ -shared -Wl,-install_name,./cpp/CPP.so -o ./cpp/CPP.so ./cpp/CPP.o


"""


import time
import gc
from ctypes import *

# A class for a C++ vector with a changepoint function in Python


def create_lib(n):
    class Vector(object):
        lib = cdll.LoadLibrary('./cpp/CPP.so')  # class level loading lib
        lib.new_vector.restype = c_void_p
        lib.new_vector.argtypes = [c_int]
        lib.delete_vector.restype = None
        lib.delete_vector.argtypes = [c_void_p]
        lib.vector_size.restype = c_int
        lib.vector_size.argtypes = [c_void_p]
        lib.vector_get.restype = c_double
        lib.vector_get.argtypes = [c_void_p, c_int]
        lib.vector_push_back.restype = None
        lib.vector_push_back.argtypes = [c_void_p, c_double]
        lib.CUMSUM.argtypes = [c_void_p, c_double * n, c_int]
        lib.CUMSUM.restype = None

        def __init__(self, length):
            self.vector = Vector.lib.new_vector(c_int(length))  # pointer to new vector

        def __del__(self):  # when reference count hits 0 in Python,
            if Vector:
                Vector.lib.delete_vector(self.vector)  # call C++ vector destructor

        def __len__(self):
            return Vector.lib.vector_size(self.vector)

        def __getitem__(self, i):  # access elements in vector at index
            if 0 <= i < len(self):
                return Vector.lib.vector_get(self.vector, c_int(i))
            raise IndexError('Vector index out of range')

        def __repr__(self):
            return '[{}]'.format(', '.join(str(self[i]) for i in range(len(self))))

        def push(self, j):  # push calls vector's push_back
            Vector.lib.vector_push_back(self.vector, c_double(j))

        def CUMSUM(self, seq):  # foo in Python calls foo in C++
            arr = (c_double * len(seq))(*seq)
            Vector.lib.CUMSUM(self.vector, arr, c_int(len(seq)))

    return Vector


class CppCUMSUM:

    def __init__(self, seq):
        gc.collect()

        start = time.time()
        Vector = create_lib(len(seq))
        cppcumsum = Vector(len(seq))

        loc = cppcumsum.CUMSUM(seq)

        number = len(seq)

        self.cumsum = []
        for n in range(number):
            self.cumsum.append(float(cppcumsum[n]))
        self.duration = time.time() - start

        del cppcumsum
