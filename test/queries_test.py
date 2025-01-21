import pytest
from db.queries.room_types import get_room_id_by_name, will_room_connect

def test_get_room_id_by_name():
    assert get_room_id_by_name("Living Room") == 2

def test_get_room_id_by_name_negative():
    with pytest.raises(ValueError):
        get_room_id_by_name("Invalid Room")
def test_will_room_connect():
    assert will_room_connect("Living Room", "Kitchen") == True
    assert will_room_connect("Kitchen", "Living Room") == True
    assert will_room_connect("Living Room", "Outside") == True

def test_will_room_connect_negative():
    assert will_room_connect("Living Room", "Bedroom") == False
    assert will_room_connect("Bedroom", "Living Room") == False
    assert will_room_connect("Bathroom", "Outside") == False

def test_will_room_connect_self():
    assert will_room_connect("Living Room", "Living Room") == False

def test_will_room_connect_invalid_room():
    with pytest.raises(ValueError):
        will_room_connect("Living Room", "Invalid Room")