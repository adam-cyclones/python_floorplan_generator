import sqlite3

conn = sqlite3.connect('db/rules.db')
cursor = conn.cursor()


def get_room_id_by_name(room_type_name: str) -> int:
    try:
        result = cursor.execute('SELECT id FROM room_types WHERE name = ?', (room_type_name,)).fetchone()
        if result is None:
            raise ValueError(f"Room type '{room_type_name}' not found")
        return result[0]
    except sqlite3.OperationalError:
        raise ValueError(f"Room type '{room_type_name}' not found")
def will_room_connect(room_a_name: str, room_b_name: str) -> bool:
    room_a_id = get_room_id_by_name(room_a_name)
    room_b_id = get_room_id_by_name(room_b_name)
    
    try:
        cursor.execute('''
            SELECT 1
            FROM connections
            WHERE 
                (from_room_id = ? AND to_room_id = ?) OR
                (from_room_id = ? AND to_room_id = ?)
            ''', (room_a_id, room_b_id, room_b_id, room_a_id))
        
        if cursor.fetchone() is not None:
            return True
        # Room types can connect
        return False
    except sqlite3.OperationalError:
        # Room types cannot connect
        return False