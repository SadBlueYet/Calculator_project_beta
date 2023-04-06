#include "my_module.hpp"
#define PI 3.14159265


namespace py = pybind11;

PYBIND11_MODULE(_my_module, m) {
        m.def("exitString", exitString);
        m.def("valueProcessing", valueProcessing);
}
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
class Stack {
public:
    std::string stringOfoperators;
    std::stack <char> operators;
    int counter = 0;
    void stackPush(char oper);
    void stackPopAndPush(char oper);
};
void Stack::stackPush(char oper) {
    operators.push(oper);
}
void Stack::stackPopAndPush(char oper) {
    stringOfoperators = "";
    counter = 0;
    do {
        if (operators.size() == 0) break;
        if ((oper == '+' || oper == '-') && operators.top() == '(') break;
        if ((oper == '*' || oper == '/') && (operators.top() == '+' || operators.top() == '-' || operators.top() == '(' || operators.size() == 0)) break;
        if (oper == '^' && operators.size() == 0) break;
        if (oper == ')' && operators.top() == '(') {
            operators.pop();
            break;
        }
        stringOfoperators += operators.top();
        stringOfoperators += ' ';
        counter += 2;
        operators.pop();
    } while (true);
    if (oper != ')') operators.push(oper);
}

std::string strCheck(std::string str) {
    std::string bufptr = "";
    for (int k = 0; k < str.length(); k++) {
        if (str[k] == '/' && str[k + 1] == '0') return "NAN";
        if (str[k] == '(' && str[k + 1] == '-') {
            bufptr += str[k];
            k++;
            bufptr += (char)48; // '0'
        }
        if ((isdigit(str[k]) && str[k + 1] == '(') || (str[k] == ')' && str[k + 1] == '(')
            || (isdigit(str[k]) && str[k + 1] == 's') || (isdigit(str[k]) && str[k + 1] == 'S')
            || (isdigit(str[k]) && str[k + 1] == 'c') || (isdigit(str[k]) && str[k + 1] == 't')) {
            bufptr += str[k];
            bufptr += (char)42; // '*'
            continue;
        }
        if (k == 0) {
            if ((str[k] == 'S' && str[k + 1] == 'Q') || (str[k] == 's' && str[k + 1] == 'i')
                || (str[k] == 'c' && str[k + 1] == 'o') || (str[k] == 'c' && str[k + 1] == 't')
                || (str[k] == 't' && str[k + 1] == 'a')) {
                bufptr += (char)48;
                bufptr += (char)43; // '+'
            }
        }
        bufptr += str[k];
    }
    return bufptr;
}
double exitString(std::string str) {
    Stack stack;
    Math* math;
    std::string num = "", exiString = "", operatr = "", value, bufptr = "";
    double val, result, counterBracketOpen, counterBracketClosed;
    int i = 0;
    bufptr = strCheck(str);
    if (bufptr == "NAN") return NAN;
    

    do {
        counterBracketClosed = 0;
        counterBracketOpen = 0;
        if (isdigit(bufptr[i])) {
            exiString += bufptr[i];
            i++;
            if (isdigit(bufptr[i]) || (bufptr[i] == '.' || bufptr[i] == ',')) {
                do {
                    if (bufptr[i] == '.' || bufptr[i] == ',') {
                        exiString += '.';
                        i++;
                    }
                    exiString += bufptr[i];
                    i++;

                } while (isdigit(bufptr[i]) || (bufptr[i] == '.' || bufptr[i] == ','));

            }
            exiString += ' ';
        }

        else {
            if (i == 0 && bufptr[i] == '-') {
                exiString += bufptr[i];
                i++;
            }
            if ((stack.operators.empty() || bufptr[i] == '(' || bufptr[i] == '^') && bufptr[i] != 's') {
                stack.stackPush(bufptr[i]);
                i++;
            }
            else {
                value = "";
                int count = 0;
                if (bufptr[i] == 's' || bufptr[i] == 'S') { // ТРИГАНОМЕТРИЯ
                    i++;
                    if (bufptr[i] == 'q' || bufptr[i] == 'Q') {
                        while (!isdigit(bufptr[i])) {
                            if (bufptr[i] == '(') break;
                            i++;
                        }
                        do {
                            if (bufptr[i] == ')') counterBracketClosed++;
                            else if (bufptr[i] == '(') counterBracketOpen++;
                            value += (char)bufptr[i];
                            i++;
                        } while (counterBracketOpen != counterBracketClosed);

                        val = exitString(value);
                        math = new Math();
                        val = math->sqrt(val);
                        delete(math);
                        exiString += std::to_string(val) + " ";
                        continue;
                    }
                    if (bufptr[i] == 'i' || bufptr[i] == 'I') {
                        while (!isdigit(bufptr[i])) {
                            if (bufptr[i] == '(') break;
                            i++;
                        }
                        do {
                            if (bufptr[i] == ')') counterBracketClosed++;
                            else if (bufptr[i] == '(') counterBracketOpen++;
                            value += (char)bufptr[i];
                            i++;
                        } while (counterBracketOpen != counterBracketClosed);

                        val = exitString(value);
                        math = new Math();
                        val = math->sin(val);
                        delete(math);
                        exiString += std::to_string(val) + " ";
                        continue;
                    }
                }
                else if (bufptr[i] == 'c' || bufptr[i] == 'C') {
                    i++;
                    if (bufptr[i] == 'o' || bufptr[i] == 'O') {
                        while (!isdigit(bufptr[i])) {
                            if (bufptr[i] == '(') break;
                            i++;
                        }
                        do {
                            if (bufptr[i] == ')') counterBracketClosed++;
                            else if (bufptr[i] == '(') counterBracketOpen++;
                            value += (char)bufptr[i];
                            i++;
                        } while (counterBracketOpen != counterBracketClosed);

                        val = exitString(value);
                        math = new Math();
                        val = math->cos(val);
                        delete(math);
                        exiString += std::to_string(val) + " ";
                        continue;
                    }
                    if (bufptr[i] == 't' || bufptr[i] == 'T') {
                        i++;
                        if (bufptr[i] == 'g' || bufptr[i] == 'G') {
                            while (!isdigit(bufptr[i])) {
                                if (bufptr[i] == '(') break;
                                i++;
                            }
                            do {
                                if (bufptr[i] == ')') counterBracketClosed++;
                                else if (bufptr[i] == '(') counterBracketOpen++;
                                value += (char)bufptr[i];
                                i++;
                            } while (counterBracketOpen != counterBracketClosed);

                            val = exitString(value);
                            math = new Math();
                            val = math->ctg(val);
                            delete(math);
                            exiString += std::to_string(val) + " ";
                            continue;
                        }
                    }
                }
                else if (bufptr[i] == 't' || bufptr[i] == 'T') {
                    while (!isdigit(bufptr[i])) {
                        if (bufptr[i] == '(') break;
                        i++;
                    }
                    do {
                        if (bufptr[i] == ')') counterBracketClosed++;
                        else if (bufptr[i] == '(') counterBracketOpen++;
                        value += (char)bufptr[i];
                        i++;
                    } while (counterBracketOpen != counterBracketClosed);

                    val = exitString(value);
                    math = new Math();
                    val = math->tan(val);
                    delete(math);
                    exiString += std::to_string(val) + " ";
                    continue;
                }
                else {
                    stack.stackPopAndPush(bufptr[i]);
                    exiString += stack.stringOfoperators;
                    i++;
                    continue;
                }
                stack.stackPush(bufptr[i]);
                i++;
            }
        }
    } while (i < bufptr.length());

    if (stack.operators.size() != 0) {
        do {
            exiString += stack.operators.top();
            exiString += ' ';
            stack.operators.pop();
        } while (stack.operators.size() != 0);
    }
    result = mathOperations(exiString);
    return result;
}

double mathOperations(std::string a) {
    std::istringstream str(a);
    std::stack<double> numbers;
    double value;
    char oper;
    double right, left;
    while (!str.eof())
    {
        while (str >> value) {
            numbers.push(value);
        }
        if (!str.eof()) {
            str.clear();
            str.unget();
            str >> oper;

            if (numbers.size() < 2) return NAN;

            right = numbers.top();
            numbers.pop();
            left = numbers.top();
            numbers.pop();
            if (oper == '+') numbers.push(left + right);
            if (oper == '-') numbers.push(left - right);
            if (oper == '*') numbers.push(left * right);
            if (oper == '/') numbers.push(left / right);
            if (oper == '^') numbers.push(pow(left, right));
        }
    }
    return numbers.top();

}
std::string valueProcessing(double value) {
    std::string str = std::to_string(value);
    std::string val = "";

    for (int i = 0; i <= str.length(); i++) {
        if (str[i] == '.' && str[i + 1] == '0') break;
        if (str[i] == '.' && str[i + 1] != '0') {
            for (int j = i; j < i + 4; j++) {
                if (str[j] == '0' && str[j + 1] == '0') break;
                val += str[j];
            }
            break;
        }
        val += str[i];
    }
    return val;
}