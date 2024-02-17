import sqlite3

connection = sqlite3.connect("data.db")
connection.row_factory = sqlite3.Row  # doing this to get the results from select query as an dict


def create_table():
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);"
        )


def add_entry(content, date):
    with connection:
        connection.execute(f"INSERT INTO entries VALUES (?,?);", (content, date))


def get_entries():
    cursor = connection.execute("SELECT * FROM entries;")
    return cursor
