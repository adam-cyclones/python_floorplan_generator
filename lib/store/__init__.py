from dataclasses import dataclass


@dataclass
class Store:
    floor_counter: str = 0
    room_counter: str = 0

    def incr_floor(self):
        self.floor_counter += 1

    def incr_room(self):
        self.room_counter += 1

    def get_floor(self):
        return self.floor_counter

    def get_room(self):
        return self.room_counter


store = Store()
