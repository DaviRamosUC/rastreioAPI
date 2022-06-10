# @file db_sqlite3.py
# Imports
import sqlite3


def monta_tabelas():
    """
    Função responsável por montar tabela de persistência dos dados do rastreio
    """
    try:
        conn = sqlite3.connect('database.db')
        conn.execute(
            'CREATE TABLE IF NOT EXISTS rastreio (codigo TEXT, numero TEXT, status TEXT)')
    except sqlite3.DatabaseError as e:
        print(e)
    finally:
        conn.close()


def insere_rastreio(codigo, numero, status):
    """
    Função responsável por inserir os dados na tabela
    :param codigo: String contendo o código de rastreio informado pelo usuário
    :param numero: String contendo o número de proprietário
    :param status: String contendo o último status do rastreio
    """
    try:
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO rastreio (codigo, numero, status) VALUES (?,?,?)', (codigo, numero, status))
        conn.commit()
    except sqlite3.DatabaseError as e:
        print(e)
    finally:
        conn.close()


def remove_rastreio(codigo):
    """
    Função responsável por remover um rastreio da tabela por um código
    :param codigo: String contendo o código de rastreio informado pelo usuário
    :return String
    """
    try:
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute('DELETE FROM rastreio WHERE codigo=?', (codigo,))
        conn.commit()
        return 'Código deletado com sucesso!'
    except sqlite3.DatabaseError as e:
        return 'Houve um erro inesperado ao remover o código'
    finally:
        conn.close()


def select_rastreio(codigo):
    """
    Função responsável por pesquisar um dado na tabela
    :param codigo: String contendo o código de rastreio informado pelo usuário
    :return Tuple
    """
    try:
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM rastreio WHERE codigo = ?', (codigo,))
        return cur.fetchall()
    except sqlite3.DatabaseError as e:
        print(e)
    finally:
        conn.close()


def selectAll_rastreio():
    """
    Função responsável por buscar todos os dados na tabela
    :return Tuple
    """
    try:
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM rastreio')
        return cur.fetchall()
    except sqlite3.DatabaseError as e:
        print(e)
    finally:
        conn.close()


def atualiza_rastreio(codigo, ultimoStatus):
    """
    Função responsável por atualizar um dado na tabela a partir de um determinado código
    :param codigo: String contendo o código de rastreio informado pelo usuário
    """
    try:
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute('UPDATE rastreio SET status = ? WHERE codigo = ?', (ultimoStatus,codigo))
        conn.commit()
    except sqlite3.DatabaseError as e:
        print(e)
    finally:
        conn.close()