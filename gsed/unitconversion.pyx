# distutils: language = c++

cdef extern from "gsed/unitconversion_cpp.h":
    double magToJy_cpp(double magnitude)

def cmagToJy(double magnitude):
    return magToJy_cpp(magnitude)
