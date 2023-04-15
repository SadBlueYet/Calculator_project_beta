#define PI 3.14159265
#include <iostream>
#include <cmath>
class Math {
private:
    double eps = 0.0001;
public:

    const int n = 10; //кол-во чисел ряда Тейлора

    double sqrt(double x) {
        double xn = x;
        double xn1 = xn - (xn * xn - x) / (2 * xn);
        while (abs(xn1 - xn) > eps) {
            xn = xn1;
            xn1 = xn - (xn * xn - x) / (2 * xn);
        }
        return xn1;
    }
    double sin(double x) {
        x *= PI / 180;
        double result = 0;
        for (int i = 0; i < n; i++) {
            result += pow(-1, i) * pow(x, 2 * i + 1) / tgamma(2 * i + 2); //tgamma() - нахождение факториала
        }
        return result;
    }
    double cos(double x) {
        x *= PI / 180;
        double result = 1;
        double term = 1;
        int sign = -1;
        for (int k = 2; k <= n; k += 2) {
            term *= x * x / ((k - 1) * k);
            result += sign * term;
            sign = -sign;
        }
        return result;
    }
    double tan(double x) {
        return sin(x) / cos(x);
    }
    double ctg(double x) {
        return cos(x) / sin(x);
    }
    ~Math() {}
};




