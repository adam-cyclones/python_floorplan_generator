from lib.store import store
from lib.data.Room import Room
from typing import List
from lib.data.Size import Size


from lib.store import store
from lib.data.Size import Size
from lib.data.Metadata import Metadata

class Floor:
    size: Size
    metadata: Metadata
    
    def __init__(self, rooms: List[Room]) -> None:
        count = store.incr_room()
        self.metadata = Metadata(
            id=f'floor_{count}',
            human_name=f'Floor {count}'
        )
        self.rooms = rooms
        self.size = Size(0, 0)
    
    def set_size(self, width: int, height: int) -> None:
        self.size.width = width
        self.size.height = height
