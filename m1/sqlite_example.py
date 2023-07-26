import sqlite3
import queries as q


def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)


def execute_q(conn, query):
    curs = conn.cursor()
    curs.execute(query)
    return curs.fetchall()


if __name__ == '__main__':
    conn = connect_to_db()
    print(execute_q(conn, q.CREATE_TEST_TABLE)[:5])
