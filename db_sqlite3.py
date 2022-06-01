import sqlite3


def monta_tabelas():
    try:
        conn = sqlite3.connect('database.db')
        conn.execute(
            'CREATE TABLE IF NOT EXISTS rastreio (codigo TEXT, numero TEXT, status TEXT)')
    except sqlite3.DatabaseError as e:
        print(e)
    finally:
        conn.close()


def insere_rastreio(codigo, numero, status):
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
    try:
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute('DELETE FROM rastreio WHERE codigo=?', (codigo,))
        conn.commit()
    except sqlite3.DatabaseError as e:
        print(e)
    finally:
        conn.close()


def select_rastreio(codigo):
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
    try:
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute('UPDATE rastreio SET ultimoStatus = ? WHERE codigo = ?', (ultimoStatus,codigo))
        conn.commit()
    except sqlite3.DatabaseError as e:
        print(e)
    finally:
        conn.close()