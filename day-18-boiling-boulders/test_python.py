from main import BoilingBoulders


def test_part_one_search():
    """
    Method to test part one of day eighteen solution.
    """
    boil = BoilingBoulders()
    assert boil.part_one_search() == 4390


def test_part_two_search():
    """
    Method to test part two of day eighteen solution.
    """
    boil = BoilingBoulders()
    assert boil.part_two_search() == 2534
