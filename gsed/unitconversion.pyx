# distutils: language = c++
# distutils: include_dirs = gsed

cdef extern from "unitconversion_cpp.h":
    double magToJy_cpp(double magnitude)

def cmagToJy(double magnitude):
    return magToJy_cpp(magnitude)
