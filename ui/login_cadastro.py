# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_cadastro.ui'
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
    QSizePolicy, QWidget)

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
        self.frame.setStyleSheet(u"background-color: rgb(143, 191, 131);\n"
"border-radius:20px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.txt_novousuario = QLabel(self.frame)
        self.txt_novousuario.setObjectName(u"txt_novousuario")
        font = QFont()
        font.setPointSize(12)
        self.txt_novousuario.setFont(font)

        self.gridLayout_2.addWidget(self.txt_novousuario, 1, 0, 1, 1)

        self.txt_novasenha = QLabel(self.frame)
        self.txt_novasenha.setObjectName(u"txt_novasenha")
        self.txt_novasenha.setFont(font)

        self.gridLayout_2.addWidget(self.txt_novasenha, 4, 0, 1, 1)

        self.txt_login = QLabel(self.frame)
        self.txt_login.setObjectName(u"txt_login")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.txt_login.setFont(font1)

        self.gridLayout_2.addWidget(self.txt_login, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.input_senha = QLineEdit(self.frame)
        self.input_senha.setObjectName(u"input_senha")
        self.input_senha.setMouseTracking(False)
        self.input_senha.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.input_senha.setInputMask(u"")
        self.input_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_senha.setCursorPosition(0)
        self.input_senha.setDragEnabled(False)
        self.input_senha.setReadOnly(False)
        self.input_senha.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.input_senha.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.input_senha, 2, 0, 1, 1)

        self.input_usuario = QLineEdit(self.frame)
        self.input_usuario.setObjectName(u"input_usuario")
        self.input_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.input_usuario, 5, 0, 1, 1)


        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.frame)

        self.botao_entrar = QPushButton(self.frame_2)
        self.botao_entrar.setObjectName(u"botao_entrar")
        font2 = QFont()
        font2.setBold(True)
        self.botao_entrar.setFont(font2)
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
        self.txt_novousuario.setText(QCoreApplication.translate("MainWindow", u"Novo nome de usu\u00e1rio:", None))
        self.txt_novasenha.setText(QCoreApplication.translate("MainWindow", u"Nova senha:", None))
        self.txt_login.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.input_senha.setPlaceholderText("")
        self.botao_entrar.setText(QCoreApplication.translate("MainWindow", u"cadastrar", None))
    # retranslateUi

