# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
                               QLabel, QLineEdit, QMainWindow, QPushButton,
                               QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowTitle("Login")
        MainWindow.resize(400, 600)  # Tamanho inicial inspirado em mobile, mas flexível
        MainWindow.setStyleSheet(u"background-color: rgb(101, 159, 109);")

        # Widget central
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Layout principal (vertical para centralização)
        self.mainLayout = QVBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(20, 20, 20, 20)
        self.mainLayout.setSpacing(20)
        self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Frame do formulário
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.frame_2.setMaximumWidth(400)  # Largura máxima para manter o estilo Instagram

        # Layout do formulário (vertical)
        self.formLayout_2 = QVBoxLayout(self.frame_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(20, 20, 20, 20)
        self.formLayout_2.setSpacing(15)

        # Frame interno (área de login)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                 "border-radius: 10px;\n"
                                 "padding: 20px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)

        # Layout do frame interno (grid para campos)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setSpacing(10)

        # Título "LOGIN"
        self.txt_login = QLabel(self.frame)
        self.txt_login.setObjectName(u"txt_login")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.txt_login.setFont(font1)
        self.txt_login.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_2.addWidget(self.txt_login, 0, 0, 1, 2)

        # Label "Usuário"
        self.txt_usuario = QLabel(self.frame)
        self.txt_usuario.setObjectName(u"txt_usuario")
        font = QFont()
        font.setPointSize(12)
        self.txt_usuario.setFont(font)
        self.gridLayout_2.addWidget(self.txt_usuario, 1, 0, 1, 1)

        # Campo de entrada "Usuário"
        self.input_usuario = QLineEdit(self.frame)
        self.input_usuario.setObjectName(u"input_usuario")
        self.input_usuario.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
                                         "border: 1px solid rgb(200, 200, 200);\n"
                                         "border-radius: 5px;\n"
                                         "padding: 10px;")
        self.input_usuario.setPlaceholderText("Digite seu usuário")
        self.input_usuario.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_usuario.setMinimumHeight(40)
        self.gridLayout_2.addWidget(self.input_usuario, 2, 0, 1, 2)

        # Label "Senha"
        self.txt_senha = QLabel(self.frame)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setFont(font)
        self.gridLayout_2.addWidget(self.txt_senha, 3, 0, 1, 1)

        # Campo de entrada "Senha"
        self.input_senha = QLineEdit(self.frame)
        self.input_senha.setObjectName(u"input_senha")
        self.input_senha.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
                                       "border: 1px solid rgb(200, 200, 200);\n"
                                       "border-radius: 5px;\n"
                                       "padding: 10px;")
        self.input_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_senha.setPlaceholderText("Digite sua senha")
        self.input_senha.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_senha.setMinimumHeight(40)
        self.input_senha.setClearButtonEnabled(True)
        self.gridLayout_2.addWidget(self.input_senha, 4, 0, 1, 2)

        self.formLayout_2.addWidget(self.frame)

        # Estilo comum dos botões
        button_style = (u"background-color: rgb(143, 191, 131);\n"
                        "border-radius: 10px;\n"
                        "padding: 10px;\n"
                        "color: white;")
        font2 = QFont()
        font2.setBold(True)
        font2.setPointSize(12)

        # Botão "Entrar"
        self.botao_entrar = QPushButton(self.frame_2)
        self.botao_entrar.setObjectName(u"botao_entrar")
        self.botao_entrar.setFont(font2)
        self.botao_entrar.setStyleSheet(button_style)
        self.botao_entrar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.botao_entrar.setMinimumHeight(50)
        self.formLayout_2.addWidget(self.botao_entrar)

        # Botão "Cadastrar-se"
        self.botao_cadastrar = QPushButton(self.frame_2)
        self.botao_cadastrar.setObjectName(u"botao_cadastrar")
        self.botao_cadastrar.setFont(font2)
        self.botao_cadastrar.setStyleSheet(button_style)
        self.botao_cadastrar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.botao_cadastrar.setMinimumHeight(50)
        self.formLayout_2.addWidget(self.botao_cadastrar)

        # Adicionar o frame_2 ao layout principal
        self.mainLayout.addWidget(self.frame_2)
        self.mainLayout.addStretch()  # Espaço flexível para centralizar verticalmente

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Login", None))
        self.txt_usuario.setText(QCoreApplication.translate("MainWindow", u"Usuário:", None))
        self.txt_senha.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.txt_login.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.botao_entrar.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.botao_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar-se", None))

