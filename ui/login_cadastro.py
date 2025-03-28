# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, Qt, QMetaObject)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QWidget, QSpacerItem)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(975, 582)
        MainWindow.setStyleSheet("background-color: #065535;")
        
        self.centralwidget = QWidget(MainWindow)
        self.gridLayout = QGridLayout(self.centralwidget)
        
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.formLayout_2 = QFormLayout(self.frame_2)
        
        self.frame = QFrame(self.frame_2)
        self.frame.setStyleSheet("background-color: #0A6847; border-radius:20px; padding: 20px;")
        self.frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        self.gridLayout_2 = QGridLayout(self.frame)
        
        self.txt_login = QLabel("LOGIN", self.frame)
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.txt_login.setFont(font1)
        self.txt_login.setStyleSheet("color: white;")
        self.gridLayout_2.addWidget(self.txt_login, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)
        
        self.txt_novousuario = QLabel("Usuário:", self.frame)
        self.txt_novousuario.setFont(QFont("", 12))
        self.txt_novousuario.setStyleSheet("color: white;")
        self.gridLayout_2.addWidget(self.txt_novousuario, 1, 0)
        
        self.input_usuario = QLineEdit(self.frame)
        self.input_usuario.setStyleSheet("background-color: white; padding: 5px; border-radius: 5px;")
        self.gridLayout_2.addWidget(self.input_usuario, 2, 0)
        
        self.txt_novasenha = QLabel("Senha:", self.frame)
        self.txt_novasenha.setFont(QFont("", 12))
        self.txt_novasenha.setStyleSheet("color: white;")
        self.gridLayout_2.addWidget(self.txt_novasenha, 3, 0)
        
        self.input_senha = QLineEdit(self.frame)
        self.input_senha.setStyleSheet("background-color: white; padding: 5px; border-radius: 5px;")
        self.input_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.gridLayout_2.addWidget(self.input_senha, 4, 0)
        
        self.botao_entrar = QPushButton("Entrar", self.frame)
        self.botao_entrar.setStyleSheet("background-color: #FFA500; color: white; border-radius: 10px; padding: 8px; font-weight: bold;")
        self.gridLayout_2.addWidget(self.botao_entrar, 5, 0, Qt.AlignmentFlag.AlignHCenter)
        
        self.botao_voltar = QPushButton("Voltar", self.frame)
        self.botao_voltar.setStyleSheet("background-color: #FF4500; color: white; border-radius: 10px; padding: 8px; font-weight: bold;")
        self.gridLayout_2.addWidget(self.botao_voltar, 6, 0, Qt.AlignmentFlag.AlignHCenter)
        self.botao_voltar.setVisible(False)
        
        self.gridLayout_2.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 7, 0)
        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.frame)
        
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Login Futebol"))

if __name__ == "__main__":
    app = QApplication([])
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()  # Inicia maximizado para melhor adaptação à tela
    app.exec()
    