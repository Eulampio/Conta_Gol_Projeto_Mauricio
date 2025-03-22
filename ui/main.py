# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QMessageBox, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

# Importando as classes UI geradas
from login_senha import Ui_MainWindow as Ui_LoginSenha
from login_cadastro import Ui_MainWindow as Ui_LoginCadastro
from cadastro_times import Ui_MainWindow as Ui_CadastroTimes
from cadastro_jogadoreseposicoes import Ui_MainWindow as Ui_CadastroJogadores
from cadastrados import Ui_MainWindow as Ui_Cadastrados
from contador import Ui_MainWindow as Ui_Contador
# Nota: O arquivo 'resultados_jogos.ui' não foi fornecido, mas será mantido na lógica
from resultados_jogos import Ui_MainWindow as Ui_ResultadosJogos

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Gerenciamento de Jogos")
        self.resize(975, 582)

        # Dicionário para simular banco de dados de usuários e imagens dos times
        self.usuarios = {}
        self.imagens_times = {"time1": None, "time2": None}  # Armazena caminhos das imagens

        # Configurando o QStackedWidget
        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # Inicializando as telas como QMainWindow e configurando as interfaces
        self.tela_login_senha = QMainWindow()
        self.ui_login_senha = Ui_LoginSenha()
        self.ui_login_senha.setupUi(self.tela_login_senha)

        self.tela_login_cadastro = QMainWindow()
        self.ui_login_cadastro = Ui_LoginCadastro()
        self.ui_login_cadastro.setupUi(self.tela_login_cadastro)

        self.tela_cadastro_times = QMainWindow()
        self.ui_cadastro_times = Ui_CadastroTimes()
        self.ui_cadastro_times.setupUi(self.tela_cadastro_times)

        self.tela_cadastro_jogadores = QMainWindow()
        self.ui_cadastro_jogadores = Ui_CadastroJogadores()
        self.ui_cadastro_jogadores.setupUi(self.tela_cadastro_jogadores)

        self.tela_cadastrados = QMainWindow()
        self.ui_cadastrados = Ui_Cadastrados()
        self.ui_cadastrados.setupUi(self.tela_cadastrados)

        self.tela_contador = QMainWindow()
        self.ui_contador = Ui_Contador()
        self.ui_contador.setupUi(self.tela_contador)

        self.tela_resultados_jogos = QMainWindow()
        self.ui_resultados_jogos = Ui_ResultadosJogos()
        self.ui_resultados_jogos.setupUi(self.tela_resultados_jogos)

        # Adicionando as telas ao QStackedWidget
        self.stacked_widget.addWidget(self.tela_login_senha)         # Índice 0
        self.stacked_widget.addWidget(self.tela_login_cadastro)     # Índice 1
        self.stacked_widget.addWidget(self.tela_cadastro_times)     # Índice 2
        self.stacked_widget.addWidget(self.tela_cadastro_jogadores) # Índice 3
        self.stacked_widget.addWidget(self.tela_cadastrados)        # Índice 4
        self.stacked_widget.addWidget(self.tela_contador)           # Índice 5
        self.stacked_widget.addWidget(self.tela_resultados_jogos)   # Índice 6

        # Definindo a tela inicial
        self.stacked_widget.setCurrentIndex(0)

        # Conectando os botões às funções de navegação e lógica
        # Tela de Login (login_senha.ui)
        self.ui_login_senha.botao_entrar.clicked.connect(self.verificar_login)
        self.ui_login_senha.botao_cadastrar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        # Tela de Cadastro de Usuário (login_cadastro.ui)
        self.ui_login_cadastro.botao_entrar.clicked.connect(self.cadastrar_usuario)
        self.ui_login_cadastro.botao_voltar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))

        # Tela de Cadastro de Times (cadastro_times.ui)
        self.ui_cadastro_times.botao_entrar.clicked.connect(self.salvar_times)
        self.ui_cadastro_times.botao_imagem1.clicked.connect(self.adicionar_imagem_time1)
        self.ui_cadastro_times.botao_imagem2.clicked.connect(self.adicionar_imagem_time2)

        # Tela de Cadastro de Jogadores (cadastro_jogadoreseposicoes.ui)
        self.ui_cadastro_jogadores.botao_entrar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(4))
        self.ui_cadastro_jogadores.botao_adicionarnovos.clicked.connect(self.adicionar_novo_jogador)

        # Tela de Cadastrados (cadastrados.ui)
        self.ui_cadastrados.botao_entrar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(5))
        self.ui_cadastrados.botao_contagols.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(5))

        # Tela de Contador (contador.ui)
        self.ui_contador.botao_salvar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(6))
        self.ui_contador.botao_mais1.clicked.connect(self.incrementar_time1)
        self.ui_contador.txt_mais2.clicked.connect(self.incrementar_time2)
        self.carregar_imagens_contador()  # Carrega as imagens ao inicializar a tela contador

        # Tela de Resultados (resultados_jogos.ui)
        self.ui_resultados_jogos.botao_entrar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        self.ui_resultados_jogos.botao_sair.clicked.connect(self.close)

    def verificar_login(self):
        usuario = self.ui_login_senha.input_usuario.text()
        senha = self.ui_login_senha.input_senha.text()

        if not usuario or not senha:
            QMessageBox.warning(self, "Erro", "Usuário ou senha não preenchidos!")
        elif usuario in self.usuarios and self.usuarios[usuario] == senha:
            self.stacked_widget.setCurrentIndex(2)  # Vai para cadastro_times
        else:
            QMessageBox.warning(self, "Erro", "Usuário ou senha incorretos!\nCadastre-se primeiro.")

    def cadastrar_usuario(self):
        usuario = self.ui_login_cadastro.input_senha.text()  # Corrigido para input_usuario
        senha = self.ui_login_cadastro.input_usuario.text()  # Corrigido para input_senha

        if not usuario or not senha:
            QMessageBox.warning(self, "Erro", "Usuário ou senha não preenchidos!")
            self.ui_login_cadastro.botao_voltar.setVisible(True)  # Mostra o botão voltar em caso de erro
        elif usuario in self.usuarios:
            QMessageBox.warning(self, "Erro", "Usuário já existe!")
            self.ui_login_cadastro.botao_voltar.setVisible(True)
        else:
            self.usuarios[usuario] = senha
            QMessageBox.information(self, "Sucesso", "Usuário cadastrado com sucesso!\nRetornando ao login.")
            self.stacked_widget.setCurrentIndex(0)

    def salvar_times(self):
        time1 = self.ui_cadastro_times.input_time1.text()
        time2 = self.ui_cadastro_times.input_time2.text()
        if not time1 or not time2:
            QMessageBox.warning(self, "Erro", "Preencha os nomes dos dois times!")
        else:
            QMessageBox.information(self, "Sucesso", "Times salvos com sucesso!")
            self.stacked_widget.setCurrentIndex(3)  # Vai para cadastro_jogadores

    def adicionar_novo_jogador(self):
        nome = self.ui_cadastro_jogadores.input_nomejogador.text()
        posicao = self.ui_cadastro_jogadores.input_posicao.text()
        time = self.ui_cadastro_jogadores.lineEdit.text()  # Campo "Time"
        if not nome or not posicao or not time:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos do jogador!")
        else:
            QMessageBox.information(self, "Sucesso", f"Jogador {nome} adicionado ao time {time}!")
            # Aqui você poderia adicionar o jogador a uma lista ou estrutura de dados
            self.ui_cadastro_jogadores.input_nomejogador.clear()
            self.ui_cadastro_jogadores.input_posicao.clear()
            self.ui_cadastro_jogadores.lineEdit.clear()

    def incrementar_time1(self):
        current_value = int(self.ui_contador.txt_time1.text())
        new_value = current_value + 1
        self.ui_contador.txt_time1.setText(str(new_value))

    def incrementar_time2(self):
        current_value = int(self.ui_contador.txt_time2.text())
        new_value = current_value + 1
        self.ui_contador.txt_time2.setText(str(new_value))

    def adicionar_imagem_time1(self):
        arquivo, _ = QFileDialog.getOpenFileName(self, "Selecionar Imagem do Time 1", "", "Imagens (*.png *.jpg *.jpeg *.svg)")
        if arquivo:
            self.imagens_times["time1"] = arquivo
            self.carregar_imagens_contador()  # Atualiza as imagens no contador

    def adicionar_imagem_time2(self):
        arquivo, _ = QFileDialog.getOpenFileName(self, "Selecionar Imagem do Time 2", "", "Imagens (*.png *.jpg *.jpeg *.svg)")
        if arquivo:
            self.imagens_times["time2"] = arquivo
            self.carregar_imagens_contador()  # Atualiza as imagens no contador

    def carregar_imagens_contador(self):
        # Carrega a imagem do Time 1 se existir
        if self.imagens_times["time1"]:
            pixmap1 = QPixmap(self.imagens_times["time1"])
            if not pixmap1.isNull():
                self.ui_contador.img.setPixmap(pixmap1.scaled(100, 100, Qt.KeepAspectRatio))
            else:
                self.ui_contador.img.clear()
        else:
            self.ui_contador.img.clear()

        # Carrega a imagem do Time 2 se existir
        if self.imagens_times["time2"]:
            pixmap2 = QPixmap(self.imagens_times["time2"])
            if not pixmap2.isNull():
                self.ui_contador.img_2.setPixmap(pixmap2.scaled(100, 100, Qt.KeepAspectRatio))
            else:
                self.ui_contador.img_2.clear()
        else:
            self.ui_contador.img_2.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())