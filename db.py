import sqlite3

DATABASE_NAME = "diler.db"


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def cur_api(database_name=DATABASE_NAME):
    conn = sqlite3.connect(database_name)
    conn.row_factory = dict_factory
    cur = conn.cursor()
    return [cur, conn]