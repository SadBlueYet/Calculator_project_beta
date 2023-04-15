import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from view.design import Ui_MainWindow

from pyqtgraph import PlotWidget, plot

import pyqtgraph as pg

import os

import controller._my_module

import re

from math import sqrt, fabs

import numpy as np

class Calculator(QMainWindow):

    def __init__(self):
        bracket_check = 0
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.but_0.clicked.connect(lambda: self.add_digit('0'))
        self.ui.but_1.clicked.connect(lambda: self.add_digit('1'))
        self.ui.but_2.clicked.connect(lambda: self.add_digit('2'))
        self.ui.but_3.clicked.connect(lambda: self.add_digit('3'))
        self.ui.but_4.clicked.connect(lambda: self.add_digit('4'))
        self.ui.but_5.clicked.connect(lambda: self.add_digit('5'))
        self.ui.but_6.clicked.connect(lambda: self.add_digit('6'))
        self.ui.but_7.clicked.connect(lambda: self.add_digit('7'))
        self.ui.but_8.clicked.connect(lambda: self.add_digit('8'))
        self.ui.but_9.clicked.connect(lambda: self.add_digit('9'))
        self.ui.but_clear.clicked.connect(self.clear_all)
        self.ui.but_dot.clicked.connect(self.add_point)
        self.ui.but_plus.clicked.connect(lambda: self.add_temp('+'))
        self.ui.but_min.clicked.connect(lambda: self.add_temp('-'))
        self.ui.but_umn.clicked.connect(lambda: self.add_temp('*'))
        self.ui.but_del.clicked.connect(lambda: self.add_temp('/'))
        self.ui.but_ravn.clicked.connect(lambda: self.add_temp('='))
        self.ui.but_step.clicked.connect(lambda: self.add_temp('^'))
        self.ui.but_sin.clicked.connect(lambda: self.add_digit('sin('))
        self.ui.but_cos.clicked.connect(lambda: self.add_digit('cos('))
        self.ui.but_tg.clicked.connect(lambda: self.add_digit('tan('))
        self.ui.but_ctg.clicked.connect(lambda: self.add_digit('ctg('))
        self.ui.but_sqrt.clicked.connect(lambda: self.add_digit('SQRT('))
        self.ui.but_bracket_open.clicked.connect(lambda: self.add_digit('('))
        self.ui.but_bracket_closed.clicked.connect(lambda: self.add_digit(')'))
        self.ui.but_graph.clicked.connect(self.graph_check)
        self.ui.but_clear_graph.clicked.connect(self.clear_graph)
        
    def clear_graph(self):
        self.ui.graph_widget.clear()
        
    def graph_check(self):
        graph_string = self.ui.line_graph.text()
        for i in range(len(graph_string)):
            if graph_string[i] == 'x' and graph_string[i + 1] == '^' and graph_string[i + 2] == '2':
                self.parabola()
                break
            elif graph_string[i] == 'x':
                self.graph_line()
                break
            
    def graph_line(self):
        graph_string = self.ui.line_graph.text()
        x = np.linspace(-10, 10, 100)
        y = []
        for j in range(len(x)):
            string = ""
            for i in range(len(graph_string)):
                if graph_string[i] == 'x' and not graph_string[i-1].isdigit():
                    string += "1*(" + str(x[j]) + ")"
                elif graph_string[i] == 'x' and graph_string[i-1].isdigit():
                    string += "*(" + str(x[j]) + ")"
                else:
                    string += graph_string[i]
                    
            string = string[2:]
            y.append(float(controller._my_module.exitString(string.encode("utf-8"))))
        self.plot(x, y)    
    def plot(self, x, y):
        self.ui.graph_widget.plot([-100,100], [0,0])
        self.ui.graph_widget.plot([0,0], [-100,100])
        self.ui.graph_widget.plot(x, y, pen='r')
    def parabola(self):
        graph_string = self.ui.line_graph.text()
        a1 = ""
        b1 = ""
        c1 = ""
        value = ""
        for i in range(len(graph_string)):
            if graph_string[i].isdigit() and graph_string[i-1] != '^' or graph_string[i] == '-':
                value += graph_string[i]
            if graph_string[i] == '^' and graph_string[i-1] == 'x':
                a1 = value
                value = ""
            if graph_string[i] == 'x' and graph_string[i+1] != '^':
                b1 = value
                value = ""
        c1 = value
        a = int(a1)
        b = int(b1)
        c = int(c1)
        discriminant = (b * b) - (4 * a * c)
        if discriminant > 0:
            x1 = (-b + sqrt(discriminant)) / (2 * a)
            x2 = (-b - sqrt(discriminant)) / (2 * a)
            if x1 > x2:
                x = np.linspace(x2, x1, 100)
            else:
                x = np.linspace(x1, x2, 100)
        elif discriminant == 0:
            x0 = -b / (2 * a)
            x = np.linspace(x0 - 10, x0 + 10, 100)

        value_y = ""
        y = []
        
        for j in range(len(x)):
            string = ""
            for i in range(len(graph_string)):
                if graph_string[i] == 'x' and graph_string[i+1] == '^':
                    string += "*(" + str(fabs(x[j])) + "^2)"    
                elif graph_string[i] == '^':
                    pass
                elif graph_string[i-1] == '^' and graph_string[i] == '2':
                    continue
                elif graph_string[i] == 'x':
                    string += "*(" + str(x[j]) + ")"
                else:
                    string += graph_string[i]
                    
            string = string[2:]
            y.append(float(controller._my_module.exitString(string.encode("utf-8"))))
        self.plot(x, y)    
        #self.ui.graph_widget.plot(x, y, pen='r')
        
           
    def sender(self): # real signature unknown; restored from __doc__
        """ sender(self) -> PySide6.QtCore.QObject """
        pass
        
    def add_digit(self, btn_text: str) -> None:
        btn = self.sender()
        
        digit_buttons = ('but_0', 'but_1', 'but_2', 'but_3', 'but_4',
                        'but_5', 'but_6', 'but_7', 'but_8', 'but_9')

        self.ui.line_entry.setText(self.ui.line_entry.text() + btn_text)
        
    def clear_all(self) -> None:
        self.ui.line_entry.clear()
        self.ui.lbl_temp.clear()     
        
    def add_point(self) -> None:
        if '.' not in self.ui.line_entry.text():
            self.ui.line_entry.setText(self.ui.line_entry.text() + '.')
    
    def add_temp(self, btn_text: str) -> None:
        btn = self.sender()
        but = self.ui.lbl_temp.text()
        self.ui.lbl_temp.setText(but + self.ui.line_entry.text() + btn_text)
        self.ui.line_entry.clear()
        if btn_text == '=':
            string = self.ui.lbl_temp.text()
            l = len(string)
            remove_last = string[:l-1]
            value = controller._my_module.exitString(remove_last.encode("utf-8"))
            self.ui.line_entry.setText(controller._my_module.valueProcessing(value))
        

if __name__ == "__main__":
	app = QApplication(sys.argv)

	window = Calculator()
	window.show()

	sys.exit(app.exec())  
