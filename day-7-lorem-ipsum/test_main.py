from main import LoremIpsum


def test_part_one_search():
    """
    Method to test part one of day five solution.
    """
    lorem = LoremIpsum()
    assert lorem.part_one_search() == 1


def test_part_two_search():
    """
    Method to test part two of day five solution.
    """
    lorem = LoremIpsum()
    assert lorem.part_two_search() == 1
