from lib.data.Size import Size
from lib.data.Floor import Floor
from lib.data.Room import Room
from typing import List


class Building:
    size: Size
    floors: List[Floor]

    def __init__(self, width: int, height: int, floors: List[Floor]):
        self.size = Size(width, height)
        self.floors = floors

        if width < 0 or height < 0:
            raise ValueError("Building size cannot be negative")

        for floor in self.floors:
            floor.set_size(width, height)
    
    def add_roots(self):
        for floor in self.floors:
            if floor.metadata.id == "floor_1":
                root = Room("Outside")
                floor.add_root(root)
            else:
                root = Room("Stairs")
                floor.add_root(root)
    def to_dict(self):
        """Convert Building to a dictionary for JSON serialization."""
        return {
            "floors": [floor.to_dict() for floor in self.floors]
        }
