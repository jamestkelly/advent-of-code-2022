from main import DayNine


def test_part_one_search():
    """
    Method to test part one of day nine solution.
    """
    nine = DayNine()
    assert nine.part_one_search() == 1533


def test_part_two_search():
    """
    Method to test part two of day nine solution.
    """
    nine = DayNine()
    assert nine.part_two_search() == 345744
