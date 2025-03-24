# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro_times.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(975, 582)
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
        self.frame.setMinimumSize(QSize(900, 700))
        self.frame.setMaximumSize(QSize(500, 16777215))
        self.frame.setStyleSheet(u"background-color: rgb(217, 217, 217);\n"
"border-radius:20px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(True)
        self.frame_3.setStyleSheet(u"background-color: rgb(143, 191, 131);")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.input_time1 = QLineEdit(self.frame_4)
        self.input_time1.setObjectName(u"input_time1")
        self.input_time1.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.input_time1, 2, 0, 1, 1)

        self.txt_time1 = QLabel(self.frame_4)
        self.txt_time1.setObjectName(u"txt_time1")

        self.gridLayout_3.addWidget(self.txt_time1, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.txt_imagem1 = QLabel(self.frame_5)
        self.txt_imagem1.setObjectName(u"txt_imagem1")

        self.gridLayout_4.addWidget(self.txt_imagem1, 0, 0, 1, 1)

        self.botao_imagem1 = QPushButton(self.frame_5)
        self.botao_imagem1.setObjectName(u"botao_imagem1")
        self.botao_imagem1.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.botao_imagem1, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.txt_time2 = QLabel(self.frame_6)
        self.txt_time2.setObjectName(u"txt_time2")

        self.gridLayout_5.addWidget(self.txt_time2, 0, 0, 1, 1)

        self.input_time2 = QLineEdit(self.frame_6)
        self.input_time2.setObjectName(u"input_time2")
        self.input_time2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.input_time2, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.txt_imagem2 = QLabel(self.frame_7)
        self.txt_imagem2.setObjectName(u"txt_imagem2")

        self.gridLayout_6.addWidget(self.txt_imagem2, 0, 0, 1, 1)

        self.botao_imagem2 = QPushButton(self.frame_7)
        self.botao_imagem2.setObjectName(u"botao_imagem2")
        self.botao_imagem2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.botao_imagem2, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_7)


        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.frame)

        self.botao_entrar = QPushButton(self.frame_2)
        self.botao_entrar.setObjectName(u"botao_entrar")
        font1 = QFont()
        font1.setBold(True)
        self.botao_entrar.setFont(font1)
        self.botao_entrar.setStyleSheet(u"background-color: rgb(143, 191, 131);\n"
"bolder-radius:50px;")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.botao_entrar)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Times", None))
        self.txt_time1.setText(QCoreApplication.translate("MainWindow", u"Time 1:", None))
        self.txt_imagem1.setText(QCoreApplication.translate("MainWindow", u"Escudo:", None))
        self.botao_imagem1.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.txt_time2.setText(QCoreApplication.translate("MainWindow", u"Time 2:", None))
        self.txt_imagem2.setText(QCoreApplication.translate("MainWindow", u"Escudo:", None))
        self.botao_imagem2.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.botao_entrar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
    # retranslateUi

import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())