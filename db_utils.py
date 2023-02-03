import sqlite3


def get_connection():
    conn = sqlite3.connect('00_Database/World_Cup_2022')
    conn.row_factory = sqlite3.Row
    return conn


def get_all_information_matches():
    conn = get_connection()
    c = conn.cursor()

    result = c.execute('SELECT * FROM "matches"')
    return result.fetchall()


def get_all_results():
    conn = get_connection()
    c = conn.cursor()

    result = c.execute('SELECT * FROM "results"')
    return result.fetchall()


def get_all_typed_results(indeks):
    indeks = (indeks)
    conn = get_connection()
    c = conn.cursor()

    result = c.execute('SELECT * FROM "results" WHERE "user_id"= ?', (indeks,))
    return result.fetchall()
