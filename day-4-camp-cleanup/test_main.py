from main import CampCleanup


def test_part_one_game():
    """
    Method to test part one of day four solution.
    """
    camp_clean = CampCleanup()
    assert camp_clean.part_one_search() == 490


def test_part_two_game():
    """
    Method to test part two of day four solution.
    """
    camp_clean = CampCleanup()
    assert camp_clean.part_two_search() == 921
