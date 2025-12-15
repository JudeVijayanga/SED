#ifndef UNITCONVERSION_H
#define UNITCONVERSION_H

// Convert AB magnitude to mJy
// Formula: 10^(-m/2.5) * 3631 Jy * 1e3
double magToJy_cpp(double magnitude);

#endif // UNITCONVERSION_H
