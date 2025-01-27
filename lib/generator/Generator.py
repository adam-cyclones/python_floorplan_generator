import json
from lib.data.Room import Room
from lib.data.Building import Building
from db.queries.room_types import get_room_id_by_name

class Generator:
    building = None

    def __init__(self, building: Building):
        self.building = building
        # self.building = get_room_id_by_name("outside")

    def to_json(self):
        print(json.dumps(self.building.to_dict(), indent=2))