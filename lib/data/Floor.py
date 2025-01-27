from lib.store import store
from lib.data.Room import Room
from typing import List
from lib.data.Size import Size


from lib.store import store
from lib.data.Size import Size
from lib.data.Metadata import Metadata


class Floor:
    root: Room
    size: Size
    metadata: Metadata
    rooms: List[Room]

    def __init__(self, *rooms: Room) -> None:
        store.incr_floor()
        count = store.get_floor()
        self.metadata = Metadata(id=f"floor_{count}", human_name=f"Floor {count}")
        self.rooms = list(rooms)
        self.size = Size(0, 0)
    
    def add_root(self, room: Room):
        self.root = room;

    def set_size(self, width: int, height: int) -> None:
        self.size.width = width
        self.size.height = height

    def to_dict(self):
        """Convert Floor to a dictionary for JSON serialization."""
        return {
            "root": self.root.to_dict(),
            "id": self.metadata.id,
            "name": self.metadata.human_name,
            "rooms": [room.to_dict() for room in self.rooms]
        }