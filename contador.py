# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contador.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFormLayout, QFrame,
    QGridLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(975, 582)
        MainWindow.setMinimumSize(QSize(500, 500))
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet(u"background-color: rgb(101, 159, 109);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(500, 500))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_2 = QFormLayout(self.frame_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(900, 500))
        self.frame.setMaximumSize(QSize(500, 16777215))
        self.frame.setStyleSheet(u"background-color: rgb(143, 191, 131);\n"
"border-radius:20px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.input_data = QDateEdit(self.frame)
        self.input_data.setObjectName(u"input_data")
        font = QFont()
        font.setPointSize(11)
        self.input_data.setFont(font)
        self.input_data.setStyleSheet(u"background-color:rgb(255, 255, 255)")

        self.gridLayout_2.addWidget(self.input_data, 1, 0, 1, 1, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.txt_time2 = QLabel(self.frame)
        self.txt_time2.setObjectName(u"txt_time2")
        font1 = QFont()
        font1.setPointSize(45)
        self.txt_time2.setFont(font1)

        self.gridLayout_2.addWidget(self.txt_time2, 2, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.txt_mais2 = QPushButton(self.frame)
        self.txt_mais2.setObjectName(u"txt_mais2")
        self.txt_mais2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.txt_mais2, 4, 2, 1, 1)

        self.txt_time1 = QLabel(self.frame)
        self.txt_time1.setObjectName(u"txt_time1")
        self.txt_time1.setFont(font1)

        self.gridLayout_2.addWidget(self.txt_time1, 2, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.img = QLabel(self.frame)
        self.img.setObjectName(u"img")
        self.img.setPixmap(QPixmap(u"../../../Pictures/Palmeiras_logo.svg.png"))

        self.gridLayout_2.addWidget(self.img, 3, 0, 1, 1)

        self.txt_x = QLabel(self.frame)
        self.txt_x.setObjectName(u"txt_x")
        font2 = QFont()
        font2.setPointSize(25)
        self.txt_x.setFont(font2)

        self.gridLayout_2.addWidget(self.txt_x, 2, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.botao_mais1 = QPushButton(self.frame)
        self.botao_mais1.setObjectName(u"botao_mais1")
        self.botao_mais1.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.botao_mais1, 4, 0, 1, 1)

        self.img_2 = QLabel(self.frame)
        self.img_2.setObjectName(u"img_2")
        self.img_2.setPixmap(QPixmap(u"../../../Downloads/png-transparent-sport-club-corinthians-paulista-corinthians-arena-esporte-clube-corinthians-sao-paulo-fc-clube-de-regatas-do-flamengo-corinthians-thumbnail-removebg-preview.png"))

        self.gridLayout_2.addWidget(self.img_2, 3, 2, 1, 1)


        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.frame)

        self.botao_salvar = QPushButton(self.frame_2)
        self.botao_salvar.setObjectName(u"botao_salvar")
        font3 = QFont()
        font3.setBold(True)
        self.botao_salvar.setFont(font3)
        self.botao_salvar.setStyleSheet(u"background-color: rgb(143, 191, 131);\n"
"bolder-radius:50px;")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.botao_salvar)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.txt_time2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.txt_mais2.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.txt_time1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.img.setText("")
        self.txt_x.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.botao_mais1.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.img_2.setText("")
        self.botao_salvar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
    # retranslateUi

import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())