import pytest
from lib.data.Room import Room


def test_room_has_width_and_height():
    room = Room(100, 100)

    assert room.size.width == 100
    assert room.size.height == 100
