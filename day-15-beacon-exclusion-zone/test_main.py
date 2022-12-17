from main import BeaconExclusionZone


def test_part_one_search():
    """
    Method to test part one of day fifteen solution.
    """
    beacon = BeaconExclusionZone()
    assert beacon.part_one_search() == 5403290


def test_part_two_search():
    """
    Method to test part two of day fifteen solution.
    """
    beacon = BeaconExclusionZone()
    assert beacon.part_two_search() == 10291582906626
