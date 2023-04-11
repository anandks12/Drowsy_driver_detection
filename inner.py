# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inner.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)




#selected_item = ''
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(686, 435)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -10, 681, 441))
        self.frame.setStyleSheet(u"background-image: url(\"D:/DDDS/logo.jpg\")")

        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 681, 21))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 361, 681, 20))
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.comboBox = QComboBox(self.frame)

        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.comboBox.setGeometry(QRect(430, 120, 171, 22))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(10)
        font.setBold(True)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 224, 228);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(530, 189, 161, 161))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.Run = QPushButton(self.frame)
        self.Run.setObjectName(u"Run")
        self.Run.setGeometry(QRect(470, 350, 75, 24))
        self.Run.setStyleSheet(u"background-color: rgb(255, 5, 59);\n"             
"selection-color: rgb(255, 14, 50);")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 686, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"CATEGORY", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Driver drowsiness", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Change alarm sound", None))
        self.Run.setText(QCoreApplication.translate("MainWindow", u"Run", None))




    # retranslateUi

