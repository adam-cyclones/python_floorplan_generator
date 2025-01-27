import sqlite3

_conn = sqlite3.connect('db/rules.db')
_cursor = _conn.cursor()

def get_conn() -> sqlite3.Connection:
    return _conn

def get_cursor() -> sqlite3.Cursor:
    return _cursor