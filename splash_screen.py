# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QProgressBar, QSizePolicy, QWidget)

class Ui_SplashSreen(object):
    def setupUi(self, SplashSreen):
        if not SplashSreen.objectName():
            SplashSreen.setObjectName(u"SplashSreen")
        SplashSreen.resize(673, 396)
        self.centralwidget = QWidget(SplashSreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.dropshadowframe = QFrame(self.centralwidget)
        self.dropshadowframe.setObjectName(u"dropshadowframe")
        self.dropshadowframe.setGeometry(QRect(0, 10, 671, 381))
        self.dropshadowframe.setAutoFillBackground(False)
        self.dropshadowframe.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.dropshadowframe.setFrameShape(QFrame.StyledPanel)
        self.dropshadowframe.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.dropshadowframe)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 661, 21))
        self.frame.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.dropshadowframe)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 361, 661, 20))
        self.frame_3.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.dropshadowframe)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 280, 111, 20))
        self.label.setStyleSheet(u"background-color: rgb(175, 190, 255);\n"
"color: rgb(0, 0, 0);")
        self.progressBar = QProgressBar(self.dropshadowframe)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(40, 230, 551, 23))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(255, 0, 0);\n"
"    color:;\n"
"	color: rgb(0, 0, 0);\n"
"    border-style:none;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar ::chunk{\n"
"    border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.869318, y2:0.727, stop:0.494318 rgba(255, 255, 0, 206), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.frame_2 = QFrame(self.dropshadowframe)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(539, 79, 141, 191))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.dropshadowframe)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, -40, 481, 341))
        self.label_2.setPixmap(QPixmap(u"bhjyvwfx_4x.png"))
        self.label_2.setScaledContents(True)
        self.frame.raise_()
        self.frame_3.raise_()
        self.frame_2.raise_()
        self.label_2.raise_()
        self.progressBar.raise_()
        self.label.raise_()
        SplashSreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashSreen)

        QMetaObject.connectSlotsByName(SplashSreen)
    # setupUi

    def retranslateUi(self, SplashSreen):
        SplashSreen.setWindowTitle(QCoreApplication.translate("SplashSreen", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("SplashSreen", u"        LOADING....", None))
        self.label_2.setText("")
    # retranslateUi

