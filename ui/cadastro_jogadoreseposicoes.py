# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro_jogadoreseposicoes.ui'
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
        MainWindow.resize(1024, 581)
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
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.input_posicao = QLineEdit(self.frame)
        self.input_posicao.setObjectName(u"input_posicao")
        self.input_posicao.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.input_posicao, 5, 0, 1, 1)

        self.txt_time = QLabel(self.frame)
        self.txt_time.setObjectName(u"txt_time")

        self.gridLayout_2.addWidget(self.txt_time, 6, 0, 1, 1)

        self.txt_nomejogador = QLabel(self.frame)
        self.txt_nomejogador.setObjectName(u"txt_nomejogador")

        self.gridLayout_2.addWidget(self.txt_nomejogador, 2, 0, 1, 1)

        self.txt_posicao = QLabel(self.frame)
        self.txt_posicao.setObjectName(u"txt_posicao")

        self.gridLayout_2.addWidget(self.txt_posicao, 4, 0, 1, 1)

        self.input_nomejogador = QLineEdit(self.frame)
        self.input_nomejogador.setObjectName(u"input_nomejogador")
        self.input_nomejogador.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.input_nomejogador, 3, 0, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(143, 191, 131);")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txt_cadastrodejogadoreseposicoes = QLabel(self.frame_3)
        self.txt_cadastrodejogadoreseposicoes.setObjectName(u"txt_cadastrodejogadoreseposicoes")
        font = QFont()
        font.setPointSize(18)
        self.txt_cadastrodejogadoreseposicoes.setFont(font)

        self.verticalLayout.addWidget(self.txt_cadastrodejogadoreseposicoes, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame_3, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.lineEdit, 7, 0, 1, 1)


        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.frame)

        self.botao_adicionarnovos = QPushButton(self.frame_2)
        self.botao_adicionarnovos.setObjectName(u"botao_adicionarnovos")
        font1 = QFont()
        font1.setBold(True)
        self.botao_adicionarnovos.setFont(font1)
        self.botao_adicionarnovos.setStyleSheet(u"background-color: rgb(143, 191, 131);")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.botao_adicionarnovos)

        self.botao_entrar = QPushButton(self.frame_2)
        self.botao_entrar.setObjectName(u"botao_entrar")
        self.botao_entrar.setFont(font1)
        self.botao_entrar.setStyleSheet(u"background-color: rgb(143, 191, 131);\n"
"bolder-radius:50px;")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.botao_entrar)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.txt_time.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.txt_nomejogador.setText(QCoreApplication.translate("MainWindow", u"Nome do jogador:", None))
        self.txt_posicao.setText(QCoreApplication.translate("MainWindow", u"Posi\u00e7\u00e3o:", None))
        self.txt_cadastrodejogadoreseposicoes.setText(QCoreApplication.translate("MainWindow", u"Cadastro de jogadores e posi\u00e7\u00f5es", None))
        self.botao_adicionarnovos.setText(QCoreApplication.translate("MainWindow", u"Adicionar novos", None))
        self.botao_entrar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
    # retranslateUi

