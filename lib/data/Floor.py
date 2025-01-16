from lib.store import store
from lib.data.Room import Room
from typing import List
from lib.data.Size import Size


class Floor:
    size: Size
    rooms: List[Room]
    
    def __init__(self, width: int, height: int, rooms: List[Room]) -> None:
        self.size = Size(width, height)
        self.rooms = rooms

    def __post_init__(self):
        store.incr_room()
        self.id = store.get_floor()
        self.name = f'Floor {self.id}'
    
    def rename(new_name: str):
        self.name = new_name