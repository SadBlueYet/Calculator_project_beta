#ifndef _TEST_H_
#define	_TEST_H_

#include <pybind11/pybind11.h>
#include <iostream>
#include <stack>
#include <sstream>
#include <math.h>
#include <string>
#ifdef	__cplusplus
extern "C" {
#endif

class Math;
class Stack;
double exitString(std::string bufptr);
double mathOperations(std::string a);
std::string valueProcessing(double value);
std::string strCheck(std::string str);
#ifdef	__cplusplus
}
#endif

#endif	/* _TEST_H_ */