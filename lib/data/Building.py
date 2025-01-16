from lib.data.Size import Size
from lib.data.Floor import Floor
from typing import List

class Building:
    size: Size
    floors: List[Floor]
    
    def __init__(self, width: int, height: int, floors: List[Floor]):
        size = Size(width, height)