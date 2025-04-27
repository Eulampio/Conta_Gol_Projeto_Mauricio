# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
                               QLabel, QLineEdit, QMainWindow, QPushButton,
                               QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowTitle("Cadastro de Times")
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

        # Layout vertical do frame interno
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(15)

        # Frame do título
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(143, 191, 131);\n"
                                   "border-radius: 5px;")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.frame_3.setMinimumHeight(60)

        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.frame_3)

        # Frame Time 1
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.gridLayout_3 = QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(5)

        self.txt_time1 = QLabel(self.frame_4)
        self.txt_time1.setObjectName(u"txt_time1")
        self.txt_time1.setFont(QFont("Arial", 12))
        self.gridLayout_3.addWidget(self.txt_time1, 0, 0, 1, 1)

        self.input_time1 = QLineEdit(self.frame_4)
        self.input_time1.setObjectName(u"input_time1")
        self.input_time1.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
                                       "border: 1px solid rgb(200, 200, 200);\n"
                                       "border-radius: 5px;\n"
                                       "padding: 10px;")
        self.input_time1.setPlaceholderText("Nome do Time 1")
        self.input_time1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_time1.setMinimumHeight(40)
        self.gridLayout_3.addWidget(self.input_time1, 1, 0, 1, 1)

        self.verticalLayout_2.addWidget(self.frame_4)

        # Frame Imagem 1
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.gridLayout_4 = QGridLayout(self.frame_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(5)

        self.txt_imagem1 = QLabel(self.frame_5)
        self.txt_imagem1.setObjectName(u"txt_imagem1")
        self.txt_imagem1.setFont(QFont("Arial", 12))
        self.gridLayout_4.addWidget(self.txt_imagem1, 0, 0, 1, 1)

        self.botao_imagem1 = QPushButton(self.frame_5)
        self.botao_imagem1.setObjectName(u"botao_imagem1")
        self.botao_imagem1.setStyleSheet(u"background-color: rgb(143, 191, 131);\n"
                                         "border-radius: 5px;\n"
                                         "padding: 10px;\n"
                                         "color: white;")
        self.botao_imagem1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.botao_imagem1.setMinimumHeight(40)
        self.gridLayout_4.addWidget(self.botao_imagem1, 1, 0, 1, 1)

        self.verticalLayout_2.addWidget(self.frame_5)

        # Frame Time 2
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.gridLayout_5 = QGridLayout(self.frame_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(5)

        self.txt_time2 = QLabel(self.frame_6)
        self.txt_time2.setObjectName(u"txt_time2")
        self.txt_time2.setFont(QFont("Arial", 12))
        self.gridLayout_5.addWidget(self.txt_time2, 0, 0, 1, 1)

        self.input_time2 = QLineEdit(self.frame_6)
        self.input_time2.setObjectName(u"input_time2")
        self.input_time2.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
                                       "border: 1px solid rgb(200, 200, 200);\n"
                                       "border-radius: 5px;\n"
                                       "padding: 10px;")
        self.input_time2.setPlaceholderText("Nome do Time 2")
        self.input_time2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.input_time2.setMinimumHeight(40)
        self.gridLayout_5.addWidget(self.input_time2, 1, 0, 1, 1)

        self.verticalLayout_2.addWidget(self.frame_6)

        # Frame Imagem 2
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.gridLayout_6 = QGridLayout(self.frame_7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(5)

        self.txt_imagem2 = QLabel(self.frame_7)
        self.txt_imagem2.setObjectName(u"txt_imagem2")
        self.txt_imagem2.setFont(QFont("Arial", 12))
        self.gridLayout_6.addWidget(self.txt_imagem2, 0, 0, 1, 1)

        self.botao_imagem2 = QPushButton(self.frame_7)
        self.botao_imagem2.setObjectName(u"botao_imagem2")
        self.botao_imagem2.setStyleSheet(u"background-color: rgb(143, 191, 131);\n"
                                         "border-radius: 5px;\n"
                                         "padding: 10px;\n"
                                         "color: white;")
        self.botao_imagem2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.botao_imagem2.setMinimumHeight(40)
        self.gridLayout_6.addWidget(self.botao_imagem2, 1, 0, 1, 1)

        self.verticalLayout_2.addWidget(self.frame_7)

        self.formLayout_2.addWidget(self.frame)

        # Botão "Salvar"
        self.botao_entrar = QPushButton(self.frame_2)
        self.botao_entrar.setObjectName(u"botao_entrar")
        font1 = QFont()
        font1.setBold(True)
        font1.setPointSize(12)
        self.botao_entrar.setFont(font1)
        self.botao_entrar.setStyleSheet(u"background-color: rgb(143, 191, 131);\n"
                                        "border-radius: 10px;\n"
                                        "padding: 10px;\n"
                                        "color: white;")
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cadastro de Times", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Times", None))
        self.txt_time1.setText(QCoreApplication.translate("MainWindow", u"Time 1:", None))
        self.txt_imagem1.setText(QCoreApplication.translate("MainWindow", u"Escudo:", None))
        self.botao_imagem1.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.txt_time2.setText(QCoreApplication.translate("MainWindow", u"Time 2:", None))
        self.txt_imagem2.setText(QCoreApplication.translate("MainWindow", u"Escudo:", None))
        self.botao_imagem2.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.botao_entrar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))

if __name__ == "__main__":
    app = QApplication([])
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec()