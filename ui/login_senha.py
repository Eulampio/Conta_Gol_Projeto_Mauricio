# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
                               QLabel, QMainWindow, QPushButton, QSizePolicy,
                               QTreeWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowTitle("Cadastro de Jogadores")
        MainWindow.resize(975, 582)
        MainWindow.setStyleSheet(u"background-color: rgb(34, 139, 34);")  # Verde vibrante para temática de futebol

        self.centralwidget = QWidget(MainWindow)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)

        # Cabeçalho temático
        self.header = QLabel("⚽ Cadastro de Jogadores ⚽", self.centralwidget)
        font_header = QFont()
        font_header.setPointSize(24)
        font_header.setBold(True)
        self.header.setFont(font_header)
        self.header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.header.setStyleSheet("color: white; margin-bottom: 15px;")
        self.gridLayout.addWidget(self.header, 0, 0, 1, 1, Qt.AlignmentFlag.AlignCenter)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.formLayout_2 = QFormLayout(self.frame_2)
        self.formLayout_2.setContentsMargins(10, 10, 10, 10)
        self.formLayout_2.setSpacing(10)

        self.frame = QFrame(self.frame_2)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 20px; padding: 15px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(10)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setStyleSheet("background-color: rgb(50, 205, 50); border-radius: 10px;")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        self.frame_3.setMinimumHeight(80)

        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.txt_cadastrados = QLabel("Jogadores Cadastrados", self.frame_3)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.txt_cadastrados.setFont(font)
        self.txt_cadastrados.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.txt_cadastrados.setStyleSheet("color: white;")

        self.verticalLayout.addWidget(self.txt_cadastrados)
        self.verticalLayout_2.addWidget(self.frame_3)

        self.treeWidget = QTreeWidget(self.frame)
        self.treeWidget.setStyleSheet("background-color: rgb(245, 245, 245); border-radius: 10px; padding: 5px;")
        self.treeWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.treeWidget.setMinimumSize(200, 200)
        self.verticalLayout_2.addWidget(self.treeWidget)
        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.frame)

        button_style = ("background-color: rgb(50, 205, 50); border-radius: 15px; padding: 10px; color: white; font-weight: bold;")
        font1 = QFont()
        font1.setBold(True)
        font1.setPointSize(12)

        self.botao_contagols = QPushButton("Contar Gols", self.frame_2)
        self.botao_contagols.setFont(font1)
        self.botao_contagols.setStyleSheet(button_style)
        self.botao_contagols.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.botao_contagols.setMinimumHeight(50)
        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.botao_contagols)

        self.botao_entrar = QPushButton("Salvar Cadastro", self.frame_2)
        self.botao_entrar.setFont(font1)
        self.botao_entrar.setStyleSheet(button_style)
        self.botao_entrar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.botao_entrar.setMinimumHeight(50)
        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.botao_entrar)

        self.botao_voltar = QPushButton("Voltar", self.frame_2)
        self.botao_voltar.setFont(font1)
        self.botao_voltar.setStyleSheet(button_style)
        self.botao_voltar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.botao_voltar.setMinimumHeight(50)
        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.botao_voltar)

        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1, Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Cadastro de Jogadores", None))
        header = self.treeWidget.headerItem()
        header.setText(2, QCoreApplication.translate("MainWindow", "Time", None))
        header.setText(1, QCoreApplication.translate("MainWindow", "Posição", None))
        header.setText(0, QCoreApplication.translate("MainWindow", "Jogador", None))
if __name__ == "__main__":
    app = QApplication([])
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()  # Inicia maximizado para melhor adaptação à tela
    app.exec()