#ifndef _TEST_H_
#define	_TEST_H_

#include <pybind11/pybind11.h>
#include <iostream>
#include <stack>
#include <sstream>
#include <math.h>
#include <string>
#include "C:/Calculatror/module/my_math.hpp"
#ifdef	__cplusplus
std::string valueProcessing(double value);
std::string strCheck(std::string str);
extern "C" {
#endif

class Math;
class Stack;
double exitString(std::string bufptr);
double mathOperations(std::string a);

#ifdef	__cplusplus
}
#endif

#endif	/* _TEST_H_ */