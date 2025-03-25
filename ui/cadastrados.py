# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastrados.ui'
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
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

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
        self.frame_3.setMinimumSize(QSize(0, 100))
        self.frame_3.setStyleSheet(u"background-color: rgb(143, 191, 131);")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txt_cadastrados = QLabel(self.frame_3)
        self.txt_cadastrados.setObjectName(u"txt_cadastrados")
        font = QFont()
        font.setPointSize(18)
        self.txt_cadastrados.setFont(font)

        self.verticalLayout.addWidget(self.txt_cadastrados, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_2.addWidget(self.frame_3)

        self.treeWidget = QTreeWidget(self.frame)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setMinimumSize(QSize(200, 100))
        self.treeWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.treeWidget)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.frame)

        self.botao_contagols = QPushButton(self.frame_2)
        self.botao_contagols.setObjectName(u"botao_contagols")
        font1 = QFont()
        font1.setBold(True)
        self.botao_contagols.setFont(font1)
        self.botao_contagols.setStyleSheet(u"background-color: rgb(143, 191, 131);")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.botao_contagols)

        self.botao_entrar = QPushButton(self.frame_2)
        self.botao_entrar.setObjectName(u"botao_entrar")
        self.botao_entrar.setFont(font1)
        self.botao_entrar.setStyleSheet(u"background-color: rgb(143, 191, 131);\n"
"border-radius:50px;")  # Corrigido 'bolder-radius' para 'border-radius'

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.botao_entrar)

        # Novo botão "Voltar"
        self.botao_voltar = QPushButton(self.frame_2)
        self.botao_voltar.setObjectName(u"botao_voltar")
        self.botao_voltar.setFont(font1)
        self.botao_voltar.setStyleSheet(u"background-color: rgb(143, 191, 131);\n"
"border-radius:50px;")
        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.botao_voltar)

        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.txt_cadastrados.setText(QCoreApplication.translate("MainWindow", u"Cadastrados", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Time", None))
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Posi\u00e7\u00e3o", None))
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Jogador", None))
        self.botao_contagols.setText(QCoreApplication.translate("MainWindow", u"Conta gols", None))
        self.botao_entrar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.botao_voltar.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
    # retranslateUi