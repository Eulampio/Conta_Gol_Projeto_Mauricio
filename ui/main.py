# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QMessageBox, QFileDialog, QTreeWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
import mysql.connector
from mysql.connector import Error

# Importando as classes UI geradas
from login_senha import Ui_MainWindow as Ui_LoginSenha
from login_cadastro import Ui_MainWindow as Ui_LoginCadastro
from cadastro_times import Ui_MainWindow as Ui_CadastroTimes
from cadastro_jogadoreseposicoes import Ui_MainWindow as Ui_CadastroJogadores
from cadastrados import Ui_MainWindow as Ui_Cadastrados
from contador import Ui_MainWindow as Ui_Contador
from resultados_jogos import Ui_MainWindow as Ui_ResultadosJogos

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Gerenciamento de Jogos")
        self.resize(975, 582)

        self.imagens_times = {"time1": None, "time2": None}
        self.db = None
        self.cursor = None

        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  # Substitua pela sua senha real
                database="gerenciamento_jogos",
                auth_plugin='mysql_native_password'
            )
            self.cursor = self.db.cursor()
            print("Conexão com o banco de dados estabelecida com sucesso!")

            # Testa a conexão com uma query simples
            self.cursor.execute("SELECT 1")
            result = self.cursor.fetchone()
            print("Teste de conexão com o banco:", result)  # Deve exibir (1,)

        except Error as e:
            QMessageBox.critical(self, "Erro de Conexão", f"Não foi possível conectar ao banco de dados: {e}")
            return  # Interrompe a inicialização se a conexão falhar

        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

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

        self.stacked_widget.addWidget(self.tela_login_senha)         # Índice 0
        self.stacked_widget.addWidget(self.tela_login_cadastro)     # Índice 1
        self.stacked_widget.addWidget(self.tela_cadastro_times)     # Índice 2
        self.stacked_widget.addWidget(self.tela_cadastro_jogadores) # Índice 3
        self.stacked_widget.addWidget(self.tela_cadastrados)        # Índice 4
        self.stacked_widget.addWidget(self.tela_contador)           # Índice 5
        self.stacked_widget.addWidget(self.tela_resultados_jogos)   # Índice 6

        self.stacked_widget.setCurrentIndex(0)

        if self.db and self.db.is_connected():
            self.ui_login_senha.botao_entrar.clicked.connect(self.verificar_login)
            self.ui_login_senha.botao_cadastrar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
            self.ui_login_cadastro.botao_entrar.clicked.connect(self.cadastrar_usuario)
            self.ui_login_cadastro.botao_voltar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
            self.ui_cadastro_times.botao_entrar.clicked.connect(self.salvar_times)
            self.ui_cadastro_times.botao_imagem1.clicked.connect(self.adicionar_imagem_time1)
            self.ui_cadastro_times.botao_imagem2.clicked.connect(self.adicionar_imagem_time2)
            self.ui_cadastro_jogadores.botao_entrar.clicked.connect(self.salvar_jogadores_e_ir_cadastrados)
            self.ui_cadastro_jogadores.botao_adicionarnovos.clicked.connect(self.adicionar_novo_jogador)
            self.ui_cadastrados.botao_entrar.clicked.connect(self.carregar_cadastrados_e_ir_contador)
            self.ui_cadastrados.botao_contagols.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(5))
            self.ui_contador.botao_salvar.clicked.connect(self.salvar_partida)
            self.ui_contador.botao_mais1.clicked.connect(self.incrementar_time1)
            self.ui_contador.txt_mais2.clicked.connect(self.incrementar_time2)
            self.carregar_imagens_contador()
            self.ui_resultados_jogos.botao_entrar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
            self.ui_resultados_jogos.botao_sair.clicked.connect(self.close)
        else:
            QMessageBox.warning(self, "Aviso", "A aplicação está rodando sem conexão ao banco de dados.")

    def verificar_login(self):
        usuario = self.ui_login_senha.input_usuario.text().strip()
        senha = self.ui_login_senha.input_senha.text().strip()
        try:
            query = "SELECT * FROM usuarios WHERE username = %s AND password = %s"
            self.cursor.execute(query, (usuario, senha))
            if self.cursor.fetchone():
                self.stacked_widget.setCurrentIndex(2)
            else:
                QMessageBox.warning(self, "Erro", "Usuário ou senha incorretos!\nCadastre-se primeiro.")
        except Error as e:
            QMessageBox.critical(self, "Erro", f"Erro ao verificar login: {e}")

    def cadastrar_usuario(self):
        usuario = self.ui_login_cadastro.input_usuario.text().strip()
        senha = self.ui_login_cadastro.input_senha.text().strip()
        try:
            if not usuario or not senha:
                QMessageBox.warning(self, "Erro", "Usuário ou senha não preenchidos!")
                self.ui_login_cadastro.botao_voltar.setVisible(True)
                return
            query = "INSERT INTO usuarios (username, password) VALUES (%s, %s)"
            self.cursor.execute(query, (usuario, senha))
            self.db.commit()
            QMessageBox.information(self, "Sucesso", "Usuário cadastrado com sucesso!\nRetornando ao login.")
            self.stacked_widget.setCurrentIndex(0)
        except Error as e:
            if "Duplicate entry" in str(e):
                QMessageBox.warning(self, "Erro", "Usuário já existe!")
            else:
                QMessageBox.critical(self, "Erro", f"Erro ao cadastrar usuário: {e}")
            self.ui_login_cadastro.botao_voltar.setVisible(True)

    def salvar_times(self):
        time1 = self.ui_cadastro_times.input_time1.text()
        time2 = self.ui_cadastro_times.input_time2.text()
        escudo1 = self.imagens_times.get("time1", "")
        escudo2 = self.imagens_times.get("time2", "")
        try:
            if not time1 or not time2:
                QMessageBox.warning(self, "Erro", "Preencha os nomes dos dois times!")
                return
            query = "INSERT INTO times (nome, escudo) VALUES (%s, %s)"
            self.cursor.execute(query, (time1, escudo1))
            self.cursor.execute(query, (time2, escudo2))
            self.db.commit()
            print("Times inseridos com sucesso!")  # Depuração
            QMessageBox.information(self, "Sucesso", "Times salvos com sucesso!")
            self.stacked_widget.setCurrentIndex(3)
        except Error as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar times: {e}")
            print(f"Erro ao salvar times: {e}")  # Depuração

    def adicionar_novo_jogador(self):
        nome = self.ui_cadastro_jogadores.input_nomejogador.text().strip()
        posicao = self.ui_cadastro_jogadores.input_posicao.text().strip()
        time_nome = self.ui_cadastro_jogadores.lineEdit.text().strip()

        try:
            # Verifica se os campos obrigatórios estão preenchidos
            if not nome or not posicao:
                QMessageBox.warning(self, "Erro", "Os campos 'Nome' e 'Posição' são obrigatórios!")
                return

            if not time_nome:
                QMessageBox.warning(self, "Erro", "O campo 'Time' não pode estar vazio!\nDigite um time para adicionar o jogador.")
                return

            # Verifica se a conexão com o banco está ativa
            if not self.db.is_connected():
                print("Conexão com o banco de dados perdida. Tentando reconectar...")
                self.db.reconnect()
                self.cursor = self.db.cursor()

            # Verifica se o time existe no banco de dados
            query_verifica_time = "SELECT id_time FROM times WHERE nome = %s"
            self.cursor.execute(query_verifica_time, (time_nome,))
            resultado = self.cursor.fetchone()

            if not resultado:
                QMessageBox.warning(self, "Erro", f"O time '{time_nome}' não foi encontrado no banco de dados!\nCadastre o time na tela de cadastro de times primeiro.")
                return

            # Se o time existe, obtém o id_time
            id_time = resultado[0]
            print(f"ID do time encontrado: {id_time}")  # Depuração

            # Insere o jogador no banco de dados
            query_inserir = "INSERT INTO jogadores (nome, posicao, id_time) VALUES (%s, %s, %s)"
            self.cursor.execute(query_inserir, (nome, posicao, id_time))
            self.db.commit()
            print(f"Jogador '{nome}' inserido no banco com id_time {id_time}")  # Depuração

            # Verifica se o jogador foi realmente inserido
            self.cursor.execute("SELECT LAST_INSERT_ID()")
            ultimo_id = self.cursor.fetchone()[0]
            print(f"Último ID inserido: {ultimo_id}")  # Confirmação de inserção

            QMessageBox.information(self, "Sucesso", f"Jogador '{nome}' adicionado ao time '{time_nome}' com sucesso!")

            # Limpa os campos após o cadastro
            self.ui_cadastro_jogadores.input_nomejogador.clear()
            self.ui_cadastro_jogadores.input_posicao.clear()
            self.ui_cadastro_jogadores.lineEdit.clear()

            # Atualiza a tela de cadastrados imediatamente
            self.carregar_cadastrados()

        except Error as e:
            QMessageBox.critical(self, "Erro", f"Erro ao adicionar jogador: {e}")
            print(f"Erro ao adicionar jogador: {e}")  # Depuração
            self.db.rollback()  # Reverte em caso de erro

    def salvar_jogadores_e_ir_cadastrados(self):
        # Verifica se a conexão com o banco está ativa
        if not self.db.is_connected():
            print("Conexão com o banco de dados perdida. Tentando reconectar...")
            self.db.reconnect()
            self.cursor = self.db.cursor()

        self.carregar_cadastrados()  # Carrega os dados mais recentes
        self.stacked_widget.setCurrentIndex(4)  # Vai para a tela de cadastrados

    def carregar_cadastrados(self):
        try:
            # Verifica se a conexão com o banco está ativa
            if not self.db.is_connected():
                print("Conexão com o banco de dados perdida. Tentando reconectar...")
                self.db.reconnect()
                self.cursor = self.db.cursor()

            # Query para buscar os jogadores e os nomes dos times associados
            query = """
                SELECT j.nome, j.posicao, t.nome 
                FROM jogadores j 
                LEFT JOIN times t ON j.id_time = t.id_time
            """
            self.cursor.execute(query)
            resultados = self.cursor.fetchall()
            print("Resultados da query em carregar_cadastrados:", resultados)  # Depuração

            # Verifica se há resultados
            if not resultados:
                print("Nenhum jogador encontrado no banco de dados.")
                QMessageBox.information(self, "Aviso", "Nenhum jogador cadastrado ainda.")
                self.ui_cadastrados.treeWidget.clear()
                return

            # Limpa a tabela antes de adicionar novos dados
            self.ui_cadastrados.treeWidget.clear()

            # Configura as colunas do treeWidget (garantindo que estejam definidas)
            self.ui_cadastrados.treeWidget.setColumnCount(3)
            self.ui_cadastrados.treeWidget.setHeaderLabels(["Jogador", "Posição", "Time"])

            # Preenche a tabela com os dados
            for nome, posicao, time in resultados:
                item = QTreeWidgetItem(self.ui_cadastrados.treeWidget)
                item.setText(0, nome if nome else "Sem nome")  # Coluna 0: Nome do jogador
                item.setText(1, posicao if posicao else "Sem posição")  # Coluna 1: Posição
                item.setText(2, time if time else "Sem time")  # Coluna 2: Nome do time
                print(f"Adicionado à tabela: {nome}, {posicao}, {time}")  # Depuração

            # Ajusta automaticamente o tamanho das colunas
            self.ui_cadastrados.treeWidget.resizeColumnToContents(0)
            self.ui_cadastrados.treeWidget.resizeColumnToContents(1)
            self.ui_cadastrados.treeWidget.resizeColumnToContents(2)

        except Error as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar jogadores cadastrados: {e}")
            print(f"Erro em carregar_cadastrados: {e}")  # Depuração

    def carregar_cadastrados_e_ir_contador(self):
        self.carregar_cadastrados()
        self.stacked_widget.setCurrentIndex(5)

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
            self.carregar_imagens_contador()

    def adicionar_imagem_time2(self):
        arquivo, _ = QFileDialog.getOpenFileName(self, "Selecionar Imagem do Time 2", "", "Imagens (*.png *.jpg *.jpeg *.svg)")
        if arquivo:
            self.imagens_times["time2"] = arquivo
            self.carregar_imagens_contador()

    def carregar_imagens_contador(self):
        if "time1" in self.imagens_times and self.imagens_times["time1"]:
            pixmap1 = QPixmap(self.imagens_times["time1"])
            if not pixmap1.isNull():
                self.ui_contador.img.setPixmap(pixmap1.scaled(100, 100, Qt.KeepAspectRatio))
            else:
                self.ui_contador.img.clear()
        if "time2" in self.imagens_times and self.imagens_times["time2"]:
            pixmap2 = QPixmap(self.imagens_times["time2"])
            if not pixmap2.isNull():
                self.ui_contador.img_2.setPixmap(pixmap2.scaled(100, 100, Qt.KeepAspectRatio))
            else:
                self.ui_contador.img_2.clear()

    def salvar_partida(self):
        try:
            gols_time1 = int(self.ui_contador.txt_time1.text())
            gols_time2 = int(self.ui_contador.txt_time2.text())
            data_partida = self.ui_contador.input_data.date().toString("yyyy-MM-dd")
            query_times = "SELECT id_time, nome FROM times ORDER BY id_time DESC LIMIT 2"
            self.cursor.execute(query_times)
            times = self.cursor.fetchall()
            if len(times) < 2:
                QMessageBox.warning(self, "Erro", "Cadastre pelo menos dois times antes de salvar uma partida!")
                return
            id_time1, nome_time1 = times[1]
            id_time2, nome_time2 = times[0]
            query = """
                INSERT INTO partidas (id_time1, id_time2, gols_time1, gols_time2, data_partida) 
                VALUES (%s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (id_time1, id_time2, gols_time1, gols_time2, data_partida))
            self.db.commit()
            QMessageBox.information(self, "Sucesso", "Partida salva com sucesso!")
            self.carregar_resultados()
            self.stacked_widget.setCurrentIndex(6)
        except Error as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar partida: {e}")

    def carregar_resultados(self):
        try:
            query = """
                SELECT t1.nome AS time1, t2.nome AS time2, p.gols_time1, p.gols_time2, p.data_partida
                FROM partidas p
                LEFT JOIN times t1 ON p.id_time1 = t1.id_time
                LEFT JOIN times t2 ON p.id_time2 = t2.id_time
            """
            self.cursor.execute(query)
            resultados = self.cursor.fetchall()
            self.ui_resultados_jogos.treeWidget.clear()
            for time1, time2, gols_time1, gols_time2, data_partida in resultados:
                item = QTreeWidgetItem(self.ui_resultados_jogos.treeWidget)
                item.setText(0, time1)
                item.setText(1, time2)
                item.setText(2, f"{gols_time1} x {gols_time2}")
                item.setText(3, str(data_partida))
        except Error as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar resultados: {e}")

    def __del__(self):
        if hasattr(self, 'db') and self.db and self.db.is_connected():
            self.cursor.close()
            self.db.close()
            print("Conexão com o banco de dados fechada.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())