from main import TreeHouse


def test_part_one_search():
    """
    Method to test part one of day five solution.
    """
    tree_house = TreeHouse()
    assert tree_house.part_one_search() == 1533


def test_part_two_search():
    """
    Method to test part two of day five solution.
    """
    tree_house = TreeHouse()
    assert tree_house.part_two_search() == 345744
