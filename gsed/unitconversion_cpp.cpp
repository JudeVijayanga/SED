#include "unitconversion_cpp.h"
#include <cmath>

double magToJy_cpp(double magnitude)
{
    // AB magnitude to flux in mJy
    return std::pow(10.0, -magnitude / 2.5) * 3631.0 * 1e3;
}
