# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
                               QLabel, QMainWindow, QPushButton, QSizePolicy,
                               QTreeWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowTitle("Cadastro")
        MainWindow.resize(975, 582)  # Tamanho inicial sugerido, mas flexível
        MainWindow.setStyleSheet(u"background-color: rgb(101, 159, 109);")

        # Widget central
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Layout principal
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(15, 15, 15, 15)  # Margens proporcionais
        self.gridLayout.setSpacing(10)

        # Frame externo
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Layout do frame externo
        self.formLayout_2 = QFormLayout(self.frame_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(20, 20, 20, 20)
        self.formLayout_2.setSpacing(15)
        self.formLayout_2.setVerticalSpacing(20)

        # Frame interno
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(217, 217, 217);\n"
                                 "border-radius: 20px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Layout vertical do frame interno
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(10)

        # Frame do título
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(143, 191, 131);")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        self.frame_3.setMinimumHeight(80)  # Altura mínima ajustável

        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 10, 0, 10)

        self.txt_cadastrados = QLabel(self.frame_3)
        self.txt_cadastrados.setObjectName(u"txt_cadastrados")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.txt_cadastrados.setFont(font)
        self.txt_cadastrados.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.txt_cadastrados.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.verticalLayout.addWidget(self.txt_cadastrados)

        self.verticalLayout_2.addWidget(self.frame_3)

        # TreeWidget
        self.treeWidget = QTreeWidget(self.frame)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                      "border-radius: 10px;")
        self.treeWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.treeWidget.setMinimumSize(200, 200)  # Tamanho mínimo para usabilidade

        self.verticalLayout_2.addWidget(self.treeWidget)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.frame)

        # Estilo comum dos botões
        button_style = (u"background-color: rgb(143, 191, 131);\n"
                        "border-radius: 15px;\n"
                        "padding: 10px;")
        font1 = QFont()
        font1.setBold(True)
        font1.setPointSize(12)

        # Botão "Conta gols"
        self.botao_contagols = QPushButton(self.frame_2)
        self.botao_contagols.setObjectName(u"botao_contagols")
        self.botao_contagols.setFont(font1)
        self.botao_contagols.setStyleSheet(button_style)
        self.botao_contagols.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.botao_contagols.setMinimumHeight(50)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.botao_contagols)

        # Botão "Salvar"
        self.botao_entrar = QPushButton(self.frame_2)
        self.botao_entrar.setObjectName(u"botao_entrar")
        self.botao_entrar.setFont(font1)
        self.botao_entrar.setStyleSheet(button_style)
        self.botao_entrar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.botao_entrar.setMinimumHeight(50)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.botao_entrar)

        # Botão "Voltar"
        self.botao_voltar = QPushButton(self.frame_2)
        self.botao_voltar.setObjectName(u"botao_voltar")
        self.botao_voltar.setFont(font1)
        self.botao_voltar.setStyleSheet(button_style)
        self.botao_voltar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.botao_voltar.setMinimumHeight(50)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.botao_voltar)

        # Adicionar o frame_2 ao gridLayout
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1, Qt.AlignmentFlag.AlignCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.txt_cadastrados.setText(QCoreApplication.translate("MainWindow", u"Cadastrados", None))
        header = self.treeWidget.headerItem()
        header.setText(2, QCoreApplication.translate("MainWindow", u"Time", None))
        header.setText(1, QCoreApplication.translate("MainWindow", u"Posição", None))
        header.setText(0, QCoreApplication.translate("MainWindow", u"Jogador", None))
        self.botao_contagols.setText(QCoreApplication.translate("MainWindow", u"Conta gols", None))
        self.botao_entrar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.botao_voltar.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))

if __name__ == "__main__":
    app = QApplication([])
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()  # Inicia maximizado para melhor adaptação à tela
    app.exec()