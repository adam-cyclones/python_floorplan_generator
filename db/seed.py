import sqlite3
from typing import List, Dict, Tuple
from db.queries.passage_types import get_passage_id_by_name
from db.queries.db import get_conn, get_cursor

def get_room_type_id(cursor: sqlite3.Cursor, room_name: str) -> int:
    """Helper function to get room type ID by name."""
    cursor.execute('SELECT id FROM room_types WHERE name = ?', (room_name,))
    result = cursor.fetchone()
    if result is None:
        raise ValueError(f"Room type '{room_name}' not found")
    return result[0]



def seed_room_types(cursor: sqlite3.Cursor, room_types: List[str]) -> None:
    """Seed the room_types table."""
    for room_type in room_types:
        cursor.execute('INSERT OR IGNORE INTO room_types (name) VALUES (?)', (room_type,))

def seed_constraints(cursor: sqlite3.Cursor, constraints: Dict[str, int]) -> None:
    """Seed the constraints table."""
    for room_type, max_connections in constraints.items():
        cursor.execute('''
            INSERT OR IGNORE INTO constraints (room_type_id, max_connections)
            VALUES ((SELECT id FROM room_types WHERE name = ?), ?)
        ''', (room_type, max_connections))

def seed_connections(cursor: sqlite3.Cursor, connections: List[Tuple[str, str]]) -> None:
    """Seed the connections table with valid room type pairs."""
    for from_room, to_room in connections:
        from_id = get_room_type_id(cursor, from_room)
        to_id = get_room_type_id(cursor, to_room)
        cursor.execute('''
            INSERT INTO connections (from_room_id, to_room_id)
            VALUES (?, ?)
        ''', (from_id, to_id))

def seed_room_types__passage_types(cursor: sqlite3.Cursor, connection_edge: List[Tuple[str, str, bool]]) -> None:
    """Seed the join table for defining valid passageways that a room type can have"""
    for room_type, passage_type, enabled in connection_edge:
        room_type_id = get_room_type_id(cursor=cursor, room_name=room_type)
        passage_type_id = get_passage_id_by_name(passage_type)
        cursor.execute('''
            INSERT INTO room_types__passage_types (room_type_id, passage_type_id, allowed)
            VALUES (?, ?, ?)
    ''', (room_type_id, passage_type_id, enabled))

def seed_passage_types(cursor: sqlite3.Cursor, passage_types: List[str]) -> None:
    """Seed the passage_types table."""
    for passage_type in passage_types:
        cursor.execute('INSERT OR IGNORE INTO passage_types (name) VALUES (?)', (passage_type,))

def seed():
    """Main seeding function."""
    try:
        conn = get_conn()
        cursor = get_cursor()

        # Define the seed data
        room_types = ['Hallway', 'Living Room', 'Kitchen', 'Bathroom', 'Bedroom', 'Outside']
        
        constraints = {
            'Hallway': 4,      # Hallways can connect to multiple rooms
            'Living Room': 3,
            'Kitchen': 2,
            'Bathroom': 1,
            'Bedroom': 2,
            'Outside': 1
        }
        
        # Define valid connections between room types
        connections = [
            ('Hallway', 'Bathroom'),
            ('Hallway', 'Bedroom'),
            ('Hallway', 'Kitchen'),
            ('Hallway', 'Living Room'),
            ('Living Room', 'Kitchen'),
            ('Outside', 'Hallway'),
            ('Outside', 'Living Room'),
            ('Outside', 'Kitchen')
        ]

        passages = [
            'Door',
            'Arch',
            'External Door'
        ]

        room_types__passage_types = [
            ("Hallway", "Door", True),
            ("Hallway", "Arch", True),
            ("Hallway", "External Door", True),
            
            ("Living Room", "Door", True),
            ("Living Room", "Arch", True),
            ("Living Room", "External Door", True),
            
            ("Kitchen", "Door", True),
            ("Kitchen", "Arch", True),
            ("Kitchen", "External Door", True),
            
            ("Bathroom", "Door", True),
            ("Bathroom", "Arch", False),
            ("Bathroom", "External Door", False),
            
            ("Bedroom", "Door", True),
            ("Bedroom", "Arch", False),
            ("Bedroom", "External Door", False),
            
            ("Outside", "Door", False),
            ("Outside", "Arch", False),
            ("Outside", "External Door", True),
        ]

        # Perform the seeding
        seed_room_types(cursor, room_types)
        seed_passage_types(cursor, passages)
        seed_constraints(cursor, constraints)
        seed_connections(cursor, connections)
        seed_room_types__passage_types(cursor, room_types__passage_types)

        conn.commit()
        print("Database seeded successfully!")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    seed()
