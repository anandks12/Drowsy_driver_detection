from PySide6 import QtCore
from PySide6.QtGui import QColor
from inner import Ui_MainWindow
from splash_screen import Ui_SplashSreen
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow, QProgressBar, QPushButton, QSizePolicy,
                               QWidget, QGraphicsDropShadowEffect,QMessageBox)
import sys
from mmdds import on_button


counter=0



class MainWindow (QMainWindow) :
    def __init__(self):
        QMainWindow.__init__ (self)
        self.ui = Ui_MainWindow ()
        self.ui.setupUi (self)
        self.ui.Run.clicked.connect(self.on_button_click)

    def on_button_click(self):
        selected_item = self.ui.comboBox.currentText()
        if selected_item != 'Real Time Detection' and selected_item != 'Video Detection':
            msg_box = QMessageBox()
            msg_box.setText("Please select a category!")
            msg_box.setWindowTitle("Error")
            msg_box.exec()
        else:
            print(selected_item)
            on_button(selected_item)




class SplashScreen (QMainWindow) :
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashSreen()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropshadowframe.setGraphicsEffect (self.shadow)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

        self.show()

    def progress(self):
        global counter
        self.ui.progressBar.setValue (counter)
        if counter > 100:
            self.timer.stop()

            self.main = MainWindow()
            self.main.show()
            self.close()


        counter += 1






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec())
