import sqlite3
import os


def conectar():

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    caminho_banco = os.path.join(BASE_DIR, "..", "database", "babysleep.db")

    os.makedirs(os.path.dirname(caminho_banco), exist_ok=True)

    print("Banco:", caminho_banco)

    return sqlite3.connect(caminho_banco)


def criar_tabelas():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bebes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        idade INTEGER,
        peso REAL,
        altura REAL,
        data_nascimento TEXT,
        formula TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sono(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bebe TEXT,
        data TEXT,
        hora_inicio TEXT,
        hora_fim TEXT,
        tipo TEXT,
        observacao TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mamadas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bebe TEXT,
        data TEXT,
        horario TEXT,
        quantidade INTEGER,
        formula TEXT,
        observacao TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alimentacao(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bebe TEXT,
        data TEXT,
        horario TEXT,
        refeicao TEXT,
        alimento TEXT,
        quantidade TEXT,
        aceitou TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vacinas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bebe TEXT,
        nome TEXT,
        data TEXT,
        proxima TEXT,
        observacao TEXT
    )
    """)

    conexao.commit()
    conexao.close()


if __name__ == "__main__":
    criar_tabelas()
    print("Banco criado com sucesso!")