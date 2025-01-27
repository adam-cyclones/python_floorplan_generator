import sqlite3

def create_schema():
    conn = sqlite3.connect('db/rules.db')
    conn.execute('PRAGMA foreign_keys = ON;')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS room_types (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS passage_types (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS room_types__passage_types (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        room_type_id INTEGER NOT NULL,
        passage_type_id INTEGER NOT NULL,
        allowed BOOLEAN,
        FOREIGN KEY (room_type_id) REFERENCES room_types(id),
        FOREIGN KEY (passage_type_id) REFERENCES passage_types(id)
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS constraints (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        room_type_id INTEGER NOT NULL,
        max_connections INTEGER,
        FOREIGN KEY (room_type_id) REFERENCES room_types(id)
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS connections (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        from_room_id INTEGER NOT NULL,
        to_room_id INTEGER NOT NULL,
        FOREIGN KEY (from_room_id) REFERENCES room_types(id),
        FOREIGN KEY (to_room_id) REFERENCES room_types(id)
    );
    ''')


    conn.commit()
    conn.close()
