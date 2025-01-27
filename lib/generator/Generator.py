import json
from lib.data.Room import Room
from lib.data.Building import Building
from db.queries.room_types import get_room_id_by_name

class Generator:
    building = None
    num_floors: int = 1

    def __init__(self, building: Building, num_floors):
        self.building = building
        self.num_floors = num_floors
        self.building = building
        self._start()
    def _start(self):
        self.building.add_roots()
        pass
    def to_json(self):
        print(json.dumps(self.building.to_dict(), indent=2))