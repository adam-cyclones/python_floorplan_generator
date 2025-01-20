import pytest
from lib.data.Room import Room


def test_room_has_width_and_height():
    room = Room()

    room.set_size(100, 100)

    assert room.size.width == 100
    assert room.size.height == 100


def test_room_can_be_positioned():
    room = Room()

    room.set_size(100, 100)
    room.set_position(10, 10)

    assert room.position.x == 10
    assert room.position.y == 10
