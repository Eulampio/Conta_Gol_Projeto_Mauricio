# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
                               QLabel, QLineEdit, QMainWindow, QPushButton,
                               QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowTitle("Cadastro de Jogadores e Posições")
        MainWindow.resize(400, 600)  # Tamanho inicial compacto, mas flexível
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
        self.frame_2.setMaximumWidth(400)  # Largura máxima no estilo Instagram

        # Layout do formulário (vertical)
        self.formLayout_2 = QVBoxLayout(self.frame_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(20, 20, 20, 20)
        self.formLayout_2.setSpacing(15)

        # Frame interno
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

        # Frame do título
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(143, 191, 131);\n"
                                   "border-radius: 5px;")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)  # Ajustado para expansão mínima

        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)  # Margens internas para o título

        self.txt_cadastrodejogadoreseposicoes = QLabel(self.frame_3)
        self.txt_cadastrodejogadoreseposicoes.setObjectName(u"txt_cadastrodejogadoreseposicoes")
        font = QFont()
        font.setPointSize(16)  # Reduzido de 18 para facilitar ajuste
        font.setBold(True)
        self.txt_cadastrodejogadoreseposicoes.setFont(font)
        self.txt_cadastrodejogadoreseposicoes.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.txt_cadastrodejogadoreseposicoes.setWordWrap(True)  # Ativado quebra de linha automática
        self.txt_cadastrodejogadoreseposicoes.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        self.verticalLayout.addWidget(self.txt_cadastrodejogadoreseposicoes)

        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1)

        # Campo "Nome do jogador"
        self.txt_nomejogador = QLabel(self.frame)
        self.txt_nomejogador.setObjectName(u"txt_nomejogador")
        self.txt_nomejogador.setFont(QFont("Arial", 12))
        self.gridLayout_2.addWidget(self.txt_nomejogador, 1, 0, 1, 1)

        self.input_nomejogador = QLineEdit(self.frame)
        self.input_nomejogador.setObjectName(u"input_nomejogador")
        self.input_nomejogador.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
                                             "border: 1px solid rgb(200, 200, 200);\n"
                                             "border-radius: 5px;\n"
                                             "padding: 10px;")
        self.input_nomejogador.setPlaceholderText("Digite o nome do jogador")
        self.input_nomejogador.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_nomejogador.setMinimumHeight(40)
        self.gridLayout_2.addWidget(self.input_nomejogador, 2, 0, 1, 1)

        # Campo "Posição"
        self.txt_posicao = QLabel(self.frame)
        self.txt_posicao.setObjectName(u"txt_posicao")
        self.txt_posicao.setFont(QFont("Arial", 12))
        self.gridLayout_2.addWidget(self.txt_posicao, 3, 0, 1, 1)

        self.input_posicao = QLineEdit(self.frame)
        self.input_posicao.setObjectName(u"input_posicao")
        self.input_posicao.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
                                         "border: 1px solid rgb(200, 200, 200);\n"
                                         "border-radius: 5px;\n"
                                         "padding: 10px;")
        self.input_posicao.setPlaceholderText("Digite a posição")
        self.input_posicao.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_posicao.setMinimumHeight(40)
        self.gridLayout_2.addWidget(self.input_posicao, 4, 0, 1, 1)

        # Campo "Time"
        self.txt_time = QLabel(self.frame)
        self.txt_time.setObjectName(u"txt_time")
        self.txt_time.setFont(QFont("Arial", 12))
        self.gridLayout_2.addWidget(self.txt_time, 5, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
                                    "border: 1px solid rgb(200, 200, 200);\n"
                                    "border-radius: 5px;\n"
                                    "padding: 10px;")
        self.lineEdit.setPlaceholderText("Digite o time")
        self.lineEdit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.lineEdit.setMinimumHeight(40)
        self.gridLayout_2.addWidget(self.lineEdit, 6, 0, 1, 1)

        self.formLayout_2.addWidget(self.frame)

        # Estilo comum dos botões
        button_style = (u"background-color: rgb(143, 191, 131);\n"
                        "border-radius: 10px;\n"
                        "padding: 10px;\n"
                        "color: white;")
        font1 = QFont()
        font1.setBold(True)
        font1.setPointSize(12)

        # Botão "Adicionar novos"
        self.botao_adicionarnovos = QPushButton(self.frame_2)
        self.botao_adicionarnovos.setObjectName(u"botao_adicionarnovos")
        self.botao_adicionarnovos.setFont(font1)
        self.botao_adicionarnovos.setStyleSheet(button_style)
        self.botao_adicionarnovos.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.botao_adicionarnovos.setMinimumHeight(50)
        self.formLayout_2.addWidget(self.botao_adicionarnovos)

        # Botão "Salvar"
        self.botao_entrar = QPushButton(self.frame_2)
        self.botao_entrar.setObjectName(u"botao_entrar")
        self.botao_entrar.setFont(font1)
        self.botao_entrar.setStyleSheet(button_style)
        self.botao_entrar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.botao_entrar.setMinimumHeight(50)
        self.formLayout_2.addWidget(self.botao_entrar)

        # Adicionar o frame_2 ao layout principal
        self.mainLayout.addWidget(self.frame_2)
        self.mainLayout.addStretch()  # Espaço flexível para centralização vertical

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cadastro de Jogadores e Posições", None))
        self.txt_time.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.txt_nomejogador.setText(QCoreApplication.translate("MainWindow", u"Nome do jogador:", None))
        self.txt_posicao.setText(QCoreApplication.translate("MainWindow", u"Posição:", None))
        self.txt_cadastrodejogadoreseposicoes.setText(QCoreApplication.translate("MainWindow", u"Cadastro de Jogadores e Posições", None))
        self.botao_adicionarnovos.setText(QCoreApplication.translate("MainWindow", u"Adicionar novos", None))
        self.botao_entrar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))

if __name__ == "__main__":
    app = QApplication([])
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec()