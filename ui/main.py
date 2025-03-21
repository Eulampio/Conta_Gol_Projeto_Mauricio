# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PySide6.QtCore import Qt

# Import UI classes from the provided files
from login_senha import Ui_MainWindow as LoginSenhaWindow  # Importing login_senha.py
from resultados_jogos import Ui_MainWindow as ResultadosJogosWindow
from cadastro_times import Ui_MainWindow as CadastroTimesWindow
from cadastro_jogadoreseposicoes import Ui_MainWindow as CadastroJogadoresWindow
from cadastrados import Ui_MainWindow as CadastradosWindow
from contador import Ui_MainWindow as ContadorWindow

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Football Manager App")
        self.resize(975, 582)

        # Create a stacked widget to manage screen navigation
        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)

        # Initialize UI screens, starting with login_senha.py
        self.login_screen = LoginSenhaWindow()  # Create instance of login_senha.py UI
        self.resultados_screen = ResultadosJogosWindow()
        self.cadastro_times_screen = CadastroTimesWindow()
        self.cadastro_jogadores_screen = CadastroJogadoresWindow()
        self.cadastrados_screen = CadastradosWindow()
        self.contador_screen = ContadorWindow()

        # Set up UI for each screen
        self.login_widget = QMainWindow()
        self.login_screen.setupUi(self.login_widget)  # Set up login_senha.py UI
        self.resultados_widget = QMainWindow()
        self.resultados_screen.setupUi(self.resultados_widget)
        self.cadastro_times_widget = QMainWindow()
        self.cadastro_times_screen.setupUi(self.cadastro_times_widget)
        self.cadastro_jogadores_widget = QMainWindow()
        self.cadastro_jogadores_screen.setupUi(self.cadastro_jogadores_widget)
        self.cadastrados_widget = QMainWindow()
        self.cadastrados_screen.setupUi(self.cadastrados_widget)
        self.contador_widget = QMainWindow()
        self.contador_screen.setupUi(self.contador_widget)

        # Add screens to the stacked widget in the specified order
        self.stack.addWidget(self.login_widget)          # Index 0: login_senha.py (Starting screen)
        self.stack.addWidget(self.resultados_widget)     # Index 1: resultados_jogos.py
        self.stack.addWidget(self.cadastro_times_widget) # Index 2: cadastro_times.py
        self.stack.addWidget(self.cadastro_jogadores_widget) # Index 3: cadastro_jogadoreseposicoes.py
        self.stack.addWidget(self.cadastrados_widget)    # Index 4: cadastrados.py
        self.stack.addWidget(self.contador_widget)       # Index 5: contador.py

        # Connect buttons to navigation functions
        self.login_screen.botao_entrar.clicked.connect(self.go_to_resultados)  # login_senha.py "Entrar" button
        self.resultados_screen.botao_entrar.clicked.connect(self.go_to_cadastro_times)
        self.cadastro_times_screen.botao_entrar.clicked.connect(self.go_to_cadastro_jogadores)
        self.cadastro_jogadores_screen.botao_entrar.clicked.connect(self.go_to_cadastrados)
        self.cadastrados_screen.botao_entrar.clicked.connect(self.go_to_contador)
        self.contador_screen.botao_salvar.clicked.connect(self.go_to_resultados)  # Loop back

        # Set the initial screen to login_senha.py
        self.stack.setCurrentIndex(0)  # Starts with login_senha.py

    def go_to_resultados(self):
        self.stack.setCurrentIndex(1)  # Moves from login_senha.py to resultados_jogos.py

    def go_to_cadastro_times(self):
        self.stack.setCurrentIndex(2)

    def go_to_cadastro_jogadores(self):
        self.stack.setCurrentIndex(3)

    def go_to_cadastrados(self):
        self.stack.setCurrentIndex(4)

    def go_to_contador(self):
        self.stack.setCurrentIndex(5)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())