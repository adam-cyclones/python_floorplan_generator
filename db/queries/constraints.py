import sqlite3
from db.queries.room_types import get_room_id_by_name
from .db import get_conn, get_cursor

conn = get_conn()
cursor = get_cursor()
def get_max_connections(room_type_name: str) -> int:
    room_type_id = get_room_id_by_name(room_type_name)
    
    try:
        result = cursor.execute('SELECT max_connections FROM constraints WHERE room_type_id = ?', (room_type_id, )).fetchone()
        if result is None:
            raise ValueError(f"Room type '{room_type_name}' not found")
        return result[0]
    except sqlite3.OperationalError:
        raise ValueError('Cannot load constraint')