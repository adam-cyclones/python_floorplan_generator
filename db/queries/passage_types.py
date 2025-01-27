import sqlite3
from .db import get_conn, get_cursor

conn = get_conn()
cursor = get_cursor()

def get_passage_id_by_name(passage_type_name: str) -> int:
    try:
        result = cursor.execute('SELECT id FROM passage_types WHERE name = ?', (passage_type_name,)).fetchone()
        if result is None:
            raise ValueError(f"Passage type '{passage_type_name}' not found")
        return result[0]
    except sqlite3.OperationalError:
        raise ValueError(f"Passage type '{passage_type_name}' not found")