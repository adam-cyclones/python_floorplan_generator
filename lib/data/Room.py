from lib.store import store
from lib.data.Size import Size
from lib.data.Metadata import Metadata
from lib.data.Position import Position
def format_id(id: str):
    return id.lower().replace(" ", "_")
class Room:
    metadata: Metadata
    position: Position
    type: str
    size: Size

    def __init__(self, type: str) -> None:
        store.incr_room()
        count = store.get_room()
        self.metadata = Metadata(id=format_id(f"room_{type}_{count}"), human_name=f"Room: {type} ({count})")
        self.position = Position(0, 0)
        self.size = Size(0, 0)
        
        if self.validate_type(type):
            self.type = type
        else:
            raise ValueError("Invalid room type")
    
    def to_dict(self):
        """Convert Room to a dictionary for JSON serialization."""
        return {
            "id": self.metadata.id,
            "name": self.metadata.human_name,
        }

    def validate_type(self, type: str):
        return True
        # return get_room_id_by_name(type) >= 0

    def set_size(self, width: int, height: int):
        self.size.width = width
        self.size.height = height
    def set_position(self, x: int, y: int):
        self.position.x = x
        self.position.y = y