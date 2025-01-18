import pytest
from lib.data.Room import Room


def test_room_has_width_and_height():
    room = Room(100, 100, 0, 0)

    assert room.size.width == 100
    assert room.size.height == 100

def test_room_can_be_positioned():
    room = Room(100, 100, 10, 10)

    assert room.position.x == 10
    assert room.position.y == 10