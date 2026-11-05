import sqlite3

# One shared connection. The loans table holds about 4 million rows per year.
connection = sqlite3.connect("library.db", check_same_thread=False)


def query(sql, params=()):
    return connection.execute(sql, params).fetchall()
