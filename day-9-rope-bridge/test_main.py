from main import RopeBridge


def test_part_one_search():
    """
    Method to test part one of day nine solution.
    """
    rope = RopeBridge()
    assert rope.part_one_search() == 6209


def test_part_two_search():
    """
    Method to test part two of day nine solution.
    """
    rope = RopeBridge()
    assert rope.part_two_search() == 2460
