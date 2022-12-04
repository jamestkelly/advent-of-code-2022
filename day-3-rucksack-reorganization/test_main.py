from main import RucksackReorganisation


def test_part_one_game():
    """
    Method to test part one of day three solution.
    """
    rucksack = RucksackReorganisation()
    assert rucksack.part_one_search() == 8493


def test_part_two_game():
    """
    Method to test part two of day three solution.
    """
    rucksack = RucksackReorganisation()
    assert rucksack.part_two_search() == 2552
