from lib.data.Building import Building
from lib.data.Floor import Floor


def test_floor_dimensions_from_building():
    building = Building(0, 0, [Floor([])])

    assert building.size.height == building.floors[0].size.height
    assert building.size.width == building.floors[0].size.width


def test_floors_cannot_extend_beyond_building():
    floor_retroactively_set_size = Floor([])
    building = Building(10, 10, [floor_retroactively_set_size])
    floor_retroactively_set_size.set_size(10, 10)
    building = Building(10, 10, [floor_retroactively_set_size])

    assert building.size.height == building.floors[0].size.height
    assert building.size.width == building.floors[0].size.width
