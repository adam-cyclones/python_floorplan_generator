from lib.store import store
from lib.data.Size import Size
from lib.data.Metadata import Metadata

class Room:
    size: Size
    metadata: Metadata
    
    def __init__(self, width: int, height: int) -> None:
        count = store.incr_room()
        self.metadata = Metadata(
            id=f'room_{count}',
            human_name=f'Room {count}'
        )
        self.size = Size(width, height)
    
    def rename(new_name: str):
        self.name = new_name