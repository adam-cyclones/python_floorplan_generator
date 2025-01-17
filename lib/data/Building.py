from lib.data.Size import Size
from lib.data.Floor import Floor
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
