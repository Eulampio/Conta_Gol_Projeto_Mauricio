-- pip install mysql-connector-python




-- -- Criar o banco de dados
-- CREATE DATABASE gerenciamento_jogos;
-- USE gerenciamento_jogos;

-- -- Tabela de Usuários
-- CREATE TABLE usuarios (
--     id_usuario INT AUTO_INCREMENT PRIMARY KEY,
--     username VARCHAR(50) NOT NULL UNIQUE,
--     password VARCHAR(50) NOT NULL
-- );

-- -- Tabela de Times
-- CREATE TABLE times (
--     id_time INT AUTO_INCREMENT PRIMARY KEY,
--     nome VARCHAR(100) NOT NULL UNIQUE,
--     escudo VARCHAR(255) -- Caminho ou nome do arquivo da imagem
-- );

-- -- Tabela de Jogadores
-- CREATE TABLE jogadores (
--     id_jogador INT AUTO_INCREMENT PRIMARY KEY,
--     nome VARCHAR(100) NOT NULL,
--     posicao VARCHAR(50) NOT NULL,
--     id_time INT,
--     FOREIGN KEY (id_time) REFERENCES times(id_time) ON DELETE SET NULL
-- );

-- -- Tabela de Partidas
-- CREATE TABLE partidas (
--     id_partida INT AUTO_INCREMENT PRIMARY KEY,
--     id_time1 INT,
--     id_time2 INT,
--     gols_time1 INT DEFAULT 0,
--     gols_time2 INT DEFAULT 0,
--     data_partida DATE,
--     FOREIGN KEY (id_time1) REFERENCES times(id_time) ON DELETE SET NULL,
--     FOREIGN KEY (id_time2) REFERENCES times(id_time) ON DELETE SET NULL
-- );

-- -- Inserir alguns dados de exemplo (opcional)
-- INSERT INTO usuarios (username, password) VALUES 
-- ('admin', '12345'),
-- ('user1', 'senha123');

-- INSERT INTO times (nome, escudo) VALUES 
-- ('Time A', 'imagens/timeA.png'),
-- ('Time B', 'imagens/timeB.png');

-- INSERT INTO jogadores (nome, posicao, id_time) VALUES 
-- ('João', 'Atacante', 1),
-- ('Pedro', 'Goleiro', 2);

-- INSERT INTO partidas (id_time1, id_time2, gols_time1, gols_time2, data_partida) VALUES 
-- (1, 2, 2, 1, '2025-03-23');