# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(366, 509)
        MainWindow.setMinimumSize(QSize(300, 500))
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: #121212;\n"
"	font-family: Rubik;\n"
"	font-size: 16pt;\n"
"	font-weight: 600;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #888;\n"
"}\n"
"QTabWidget::pane {\n"
"  border: 1px solid lightgray;\n"
"  top:-1px; \n"
"  background: rgb(245, 245, 245);; \n"
"} \n"
"QTabBar::tab {\n"
"  background: rgb(230, 230, 230); \n"
"  border: 1px solid lightgray; \n"
"\n"
"} \n"
"QTabBar::tab:selected { \n"
"  background: rgb(245, 245, 245); \n"
"  margin-bottom: -1px; \n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabBar::tab:selected {\n"
"  background: transparent;\n"
" }\n"
"QTabBar::tab {\n"
"  background: gray;\n"
"  color: white;\n"
"\n"
" }")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.lbl_temp = QLabel(self.tab)
        self.lbl_temp.setObjectName(u"lbl_temp")
        self.lbl_temp.setGeometry(QRect(0, 0, 341, 24))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_temp.sizePolicy().hasHeightForWidth())
        self.lbl_temp.setSizePolicy(sizePolicy)
        self.lbl_temp.setStyleSheet(u"color: #888;")
        self.lbl_temp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.line_entry = QLineEdit(self.tab)
        self.line_entry.setObjectName(u"line_entry")
        self.line_entry.setGeometry(QRect(0, 30, 341, 61))
        self.line_entry.setStyleSheet(u"font-size: 40pt;\n"
"border: none;")
        self.line_entry.setMaxLength(16)
        self.line_entry.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.line_entry.setReadOnly(True)
        self.layoutWidget = QWidget(self.tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 100, 341, 361))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.but_ctg = QPushButton(self.layoutWidget)
        self.but_ctg.setObjectName(u"but_ctg")
        self.but_ctg.setMaximumSize(QSize(63, 100))

        self.gridLayout.addWidget(self.but_ctg, 4, 4, 1, 1)

        self.but_dot = QPushButton(self.layoutWidget)
        self.but_dot.setObjectName(u"but_dot")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.but_dot.sizePolicy().hasHeightForWidth())
        self.but_dot.setSizePolicy(sizePolicy1)
        self.but_dot.setMaximumSize(QSize(63, 100))

        self.gridLayout.addWidget(self.but_dot, 4, 0, 1, 1)

        self.but_step = QPushButton(self.layoutWidget)
        self.but_step.setObjectName(u"but_step")
        sizePolicy1.setHeightForWidth(self.but_step.sizePolicy().hasHeightForWidth())
        self.but_step.setSizePolicy(sizePolicy1)
        self.but_step.setMaximumSize(QSize(63, 100))

        self.gridLayout.addWidget(self.but_step, 0, 1, 1, 1)

        self.but_2 = QPushButton(self.layoutWidget)
        self.but_2.setObjectName(u"but_2")
        sizePolicy1.setHeightForWidth(self.but_2.sizePolicy().hasHeightForWidth())
        self.but_2.setSizePolicy(sizePolicy1)
        self.but_2.setMaximumSize(QSize(63, 100))

        self.gridLayout.addWidget(self.but_2, 3, 1, 1, 1)

        self.but_del = QPushButton(self.layoutWidget)
        self.but_del.setObjectName(u"but_del")
        sizePolicy1.setHeightForWidth(self.but_del.sizePolicy().hasHeightForWidth())
        self.but_del.setSizePolicy(sizePolicy1)
        self.but_del.setMaximumSize(QSize(63, 100))

        self.gridLayout.addWidget(self.but_del, 1, 3, 1, 1)

        self.but_6 = QPushButton(self.layoutWidget)
        self.but_6.setObjectName(u"but_6")
        sizePolicy1.setHeightForWidth(self.but_6.sizePolicy().hasHeightForWidth())
        self.but_6.setSizePolicy(sizePolicy1)
        self.but_6.setMaximumSize(QSize(63, 100))

        self.gridLayout.addWidget(self.but_6, 2, 2, 1, 1)

        self.but_umn = QPushButton(self.layoutWidget)
        self.but_umn.setObjectName(u"but_umn")
        sizePolicy1.setHeightForWidth(self.but_umn.sizePolicy().hasHeightForWidth())
        self.but_umn.setSizePolicy(sizePolicy1)
        self.but_umn.setMaximumSize(QSize(63, 100))

        self.gridLayout.addWidget(self.but_umn, 1, 4, 1, 1)

        self.but_sin = QPushButton(self.layoutWidget)
        self.but_sin.setObjectName(u"but_sin")
        self.but_sin.setMaximumSize(QSize(63, 100))

        self.gridLayout.addWidget(self.but_sin, 3, 3, 1, 1)

        self.but_5 = QPushButton(self.layoutWidget)
        self.but_5.setObjectName(u"but_5")
        sizePolicy1.setHeightForWidth(self.but_5.sizePolicy().hasHeightForWidth())
        self.but_5.setSizePolicy(sizePolicy1)
        self.but_5.setMaximumSize(QSize(63, 100))

        self.gridLayout.addWidget(self.but_5, 2, 1, 1, 1)

        self.but_0 = QPushButton(self.layoutWidget)
        self.but_0.setObjectName(u"but_0")
        sizePolicy1.setHeightForWidth(self.but_0.sizePolicy().hasHeightForWidth())
        self.but_0.setSizePolicy(sizePolicy1)
        self.but_0.setMaximumSize(QSize(63, 100))

        self.gridLayout.addWidget(self.but_0, 4, 1, 1, 1)

        self.but_min = QPushButton(self.layoutWidget)
        self.but_min.setObjectName(u"but_min")
        sizePolicy1.setHeightForWidth(self.but_min.sizePolicy().hasHeightForWidth())
        self.but_min.setSizePolicy(sizePolicy1)
        self.but_min.setMaximumSize(QSize(63, 100))

        self.gridLayout.addWidget(self.but_min, 2, 4, 1, 1)

        self.but_3 = QPushButton(self.layoutWidget)
        self.but_3.setObjectName(u"but_3")
        sizePolicy1.setHeightForWidth(self.but_3.sizePolicy().hasHeightForWidth())
        self.but_3.setSizePolicy(sizePolicy1)
        self.but_3.setMaximumSize(QSize(63, 100))


        self.gridLayout.addWidget(self.but_3, 3, 2, 1, 1)

        self.but_9 = QPushButton(self.layoutWidget)
        self.but_9.setObjectName(u"but_9")
        sizePolicy1.setHeightForWidth(self.but_9.sizePolicy().hasHeightForWidth())
        self.but_9.setSizePolicy(sizePolicy1)
        self.but_9.setMaximumSize(QSize(63, 100))

        self.gridLayout.addWidget(self.but_9, 1, 2, 1, 1)

        self.but_plus = QPushButton(self.layoutWidget)
        self.but_plus.setObjectName(u"but_plus")
        sizePolicy1.setHeightForWidth(self.but_plus.sizePolicy().hasHeightForWidth())
        self.but_plus.setSizePolicy(sizePolicy1)
        self.but_plus.setMaximumSize(QSize(63, 100))

        self.gridLayout.addWidget(self.but_plus, 2, 3, 1, 1)

        self.but_ravn = QPushButton(self.layoutWidget)
        self.but_ravn.setObjectName(u"but_ravn")
        sizePolicy1.setHeightForWidth(self.but_ravn.sizePolicy().hasHeightForWidth())
        self.but_ravn.setSizePolicy(sizePolicy1)
        self.but_ravn.setMaximumSize(QSize(63, 100))

        self.gridLayout.addWidget(self.but_ravn, 4, 2, 1, 1)

        self.but_tg = QPushButton(self.layoutWidget)
        self.but_tg.setObjectName(u"but_tg")
        self.but_tg.setMaximumSize(QSize(63, 100))

        self.gridLayout.addWidget(self.but_tg, 4, 3, 1, 1)

        self.but_1 = QPushButton(self.layoutWidget)
        self.but_1.setObjectName(u"but_1")
        sizePolicy1.setHeightForWidth(self.but_1.sizePolicy().hasHeightForWidth())
        self.but_1.setSizePolicy(sizePolicy1)
        self.but_1.setMaximumSize(QSize(63, 100))

        self.gridLayout.addWidget(self.but_1, 3, 0, 1, 1)

        self.but_sqrt = QPushButton(self.layoutWidget)
        self.but_sqrt.setObjectName(u"but_sqrt")
        sizePolicy1.setHeightForWidth(self.but_sqrt.sizePolicy().hasHeightForWidth())
        self.but_sqrt.setSizePolicy(sizePolicy1)
        self.but_sqrt.setMaximumSize(QSize(63, 100))

        self.gridLayout.addWidget(self.but_sqrt, 0, 2, 1, 1)

        self.but_4 = QPushButton(self.layoutWidget)
        self.but_4.setObjectName(u"but_4")
        sizePolicy1.setHeightForWidth(self.but_4.sizePolicy().hasHeightForWidth())
        self.but_4.setSizePolicy(sizePolicy1)
        self.but_4.setMaximumSize(QSize(63, 100))

        self.gridLayout.addWidget(self.but_4, 2, 0, 1, 1)

        self.but_8 = QPushButton(self.layoutWidget)
        self.but_8.setObjectName(u"but_8")
        sizePolicy1.setHeightForWidth(self.but_8.sizePolicy().hasHeightForWidth())
        self.but_8.setSizePolicy(sizePolicy1)
        self.but_8.setMaximumSize(QSize(63, 100))

        self.gridLayout.addWidget(self.but_8, 1, 1, 1, 1)

        self.but_cos = QPushButton(self.layoutWidget)
        self.but_cos.setObjectName(u"but_cos")
        self.but_cos.setMaximumSize(QSize(63, 100))

        self.gridLayout.addWidget(self.but_cos, 3, 4, 1, 1)

        self.but_7 = QPushButton(self.layoutWidget)
        self.but_7.setObjectName(u"but_7")
        sizePolicy1.setHeightForWidth(self.but_7.sizePolicy().hasHeightForWidth())
        self.but_7.setSizePolicy(sizePolicy1)
        self.but_7.setMaximumSize(QSize(63, 100))

        self.gridLayout.addWidget(self.but_7, 1, 0, 1, 1)

        self.but_clear = QPushButton(self.layoutWidget)
        self.but_clear.setObjectName(u"but_clear")
        sizePolicy1.setHeightForWidth(self.but_clear.sizePolicy().hasHeightForWidth())
        self.but_clear.setSizePolicy(sizePolicy1)
        self.but_clear.setMaximumSize(QSize(63, 100))
        self.but_clear.setStyleSheet(u"")

        self.gridLayout.addWidget(self.but_clear, 0, 0, 1, 1)

        self.but_bracket_open = QPushButton(self.layoutWidget)
        self.but_bracket_open.setObjectName(u"but_bracket_open")
        sizePolicy1.setHeightForWidth(self.but_bracket_open.sizePolicy().hasHeightForWidth())
        self.but_bracket_open.setSizePolicy(sizePolicy1)
        self.but_bracket_open.setMaximumSize(QSize(63, 100))

        self.gridLayout.addWidget(self.but_bracket_open, 0, 3, 1, 1)

        self.but_bracket_closed = QPushButton(self.layoutWidget)
        self.but_bracket_closed.setObjectName(u"but_bracket_closed")
        sizePolicy1.setHeightForWidth(self.but_bracket_closed.sizePolicy().hasHeightForWidth())
        self.but_bracket_closed.setSizePolicy(sizePolicy1)
        self.but_bracket_closed.setMaximumSize(QSize(63, 100))

        self.gridLayout.addWidget(self.but_bracket_closed, 0, 4, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.graph_widget = PlotWidget(self.tab_2)
        self.graph_widget.setObjectName(u"graph_widget")
        self.graph_widget.setGeometry(QRect(0, 0, 341, 261))
        self.line_graph = QLineEdit(self.tab_2)
        self.line_graph.setObjectName(u"line_graph")
        self.line_graph.setGeometry(QRect(0, 270, 351, 51))
        self.gridLayoutWidget = QWidget(self.tab_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 320, 351, 141))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.but_graph = QPushButton(self.gridLayoutWidget)
        self.but_graph.setObjectName(u"but_graph")
        self.but_graph.setMinimumSize(QSize(0, 60))
        self.but_graph.setMaximumSize(QSize(16777215, 16777215))
        self.but_graph.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.but_graph, 0, 0, 1, 1)

        self.but_clear_graph = QPushButton(self.gridLayoutWidget)
        self.but_clear_graph.setObjectName(u"but_clear_graph")
        self.but_clear_graph.setMinimumSize(QSize(0, 60))
        font = QFont()
        font.setFamilies([u"Rubik"])
        font.setPointSize(16)
        font.setBold(True)
        self.but_clear_graph.setFont(font)
        self.but_clear_graph.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.but_clear_graph, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.lbl_temp.setText("")
        self.line_entry.setText("")
        self.but_ctg.setText(QCoreApplication.translate("MainWindow", u"ctg", None))
        self.but_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.but_step.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.but_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.but_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.but_del.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.but_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.but_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.but_umn.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.but_sin.setText(QCoreApplication.translate("MainWindow", u"sin", None))
        self.but_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.but_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.but_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.but_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.but_min.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.but_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.but_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.but_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.but_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.but_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.but_ravn.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.but_tg.setText(QCoreApplication.translate("MainWindow", u"tan", None))
        self.but_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.but_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.but_sqrt.setText(QCoreApplication.translate("MainWindow", u"SQRT", None))
        self.but_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.but_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.but_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.but_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.but_cos.setText(QCoreApplication.translate("MainWindow", u"cos", None))
        self.but_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.but_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.but_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.but_bracket_open.setText(QCoreApplication.translate("MainWindow", u"( ", None))
        self.but_bracket_closed.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u" Calculator ", None))
        self.but_graph.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.but_clear_graph.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u" Graphics ", None))
    # retranslateUi

