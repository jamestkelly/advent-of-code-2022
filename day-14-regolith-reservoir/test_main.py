from main import RegolithReservoir


def test_part_one_search():
    """
    Method to test part one of day fourteen solution.
    """
    regolith_reservoir = RegolithReservoir()
    assert regolith_reservoir.part_one_search() == 618


def test_part_two_search():
    """
    Method to test part two of day fourteen solution.
    """
    regolith_reservoir = RegolithReservoir()
    assert regolith_reservoir.part_two_search() == 26358
