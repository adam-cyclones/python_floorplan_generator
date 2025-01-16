from dataclasses import dataclass
from .. import incr_room


@dataclass
class Room:
    floor: int = 0
    name: str = f"Floor {incr_room()}"
    width: int
    height: int

    def printName():
        print(self.name)
