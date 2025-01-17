import pytest
from lib.data.Building import Building
from lib.data.Floor import Floor


def test_building_has_width_and_height():
    building = Building(100, 100, [])

    assert building.size.width == 100
    assert building.size.height == 100


def test_building_has_floors():
    building = Building(0, 0, [Floor()])

    assert len(building.floors) == 1


def test_size_cannot_be_negative():
    with pytest.raises(ValueError):
        Building(-1, -1, [])
