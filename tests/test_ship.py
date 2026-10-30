import pytest

from statki.ship import Ship

FRIGATE = 3
SLOOP = 1


def stats(ship: Ship) -> tuple[int, int, int, int, int]:
    return ship.hull, ship.hold, ship.sails, ship.cannons, ship.crew


def test_new_ship_has_full_stats():
    assert stats(Ship(FRIGATE)) == (3, 3, 3, 3, 3)


@pytest.mark.parametrize(
    "level, expected_type",
    [(1, "Sloop"), (5, "Ship of the line"), (0, "Sloop"), (99, "Sloop")],
)
def test_ship_type_from_level(level, expected_type):
    assert Ship(level).ship_type == expected_type


@pytest.mark.parametrize(
    "location, attribute",
    [(1, "hold"), (2, "sails"), (3, "cannons"), (4, "crew")],
)
def test_damage_hits_compartment_first(location, attribute):
    ship = Ship(FRIGATE)
    ship.receive_damage([location])
    assert getattr(ship, attribute) == 2
    assert ship.hull == 3


def test_damage_spills_over_to_hull_when_compartment_is_empty():
    ship = Ship(FRIGATE)
    ship.receive_damage([1, 1, 1, 1])  # 3 hold + 1 spillover
    assert ship.hold == 0
    assert ship.hull == 2


def test_ship_is_destroyed_when_hull_reaches_zero():
    ship = Ship(FRIGATE)
    assert not ship.is_destroyed()
    ship.receive_damage([1] * 6)  # 3 hold + 3 hull
    assert ship.is_destroyed()


def test_destroyed_ship_takes_no_more_damage():
    ship = Ship(FRIGATE)
    ship.receive_damage([1] * 6 + [2, 3, 4])
    assert ship.hull == 0
    assert (ship.sails, ship.cannons, ship.crew) == (3, 3, 3)


def test_invalid_location_raises():
    with pytest.raises(ValueError):
        Ship(FRIGATE).receive_damage([89])


@pytest.mark.parametrize(
    "ship_type, level",
    [("Sloop", 1), ("Fluyt", 2), ("Frigate", 3), ("Galleon", 4), ("Ship of the line", 5)],
)
def test_determine_ship_level(ship_type, level):
    ship = Ship(level)
    assert ship.ship_type == ship_type
    assert ship.determine_ship_level() == level


def test_full_repair_restores_stats():
    ship = Ship(FRIGATE)
    ship.receive_damage([1, 2, 3, 4, 1, 1, 1])
    ship.full_repair()
    assert stats(ship) == (3, 3, 3, 3, 3)
