# Junior Obom
# 15/07/2018

print("Start")

import sqlite3

os.chdir(os.path.dirname(os.path.abspath(__file__))) # Aponta para o caminho da pasta da IA
caminho=os.getcwd()+"/IADoxoBD.db" # Monta o caminho do txt de infos

conn = sqlite3.connect(caminho) # Conectando ao banco de dados
cursor = conn.cursor() # Definindo cursor do BD


DROP table logs;

CREATE TABLE logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    descricao VARCHAR,
    t REAL DEFAULT (datetime('now', 'localtime'))
);

-- INSERT INTO "logs" DEFAULT VALUES;
insert into logs('descricao') values('teste');
SELECT * FROM logs;

