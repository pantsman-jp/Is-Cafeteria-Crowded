from sqlite3 import connect


def make_db():
    conn = connect("cafeteria_status.db")
    conn.close()


def make_table():
    conn = connect("cafeteria_status.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE vote (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp TEXT NOT NULL, ip TEXT NOT NULL, status INTEGER NOT NULL)"
    )
    conn.commit()
    conn.close()


make_db()
make_table()
