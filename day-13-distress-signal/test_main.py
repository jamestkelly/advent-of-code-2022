from main import DistressSignal


def test_part_one_game():
    """
    Method to test part one of day thirteen solution.
    """
    distress_signal = DistressSignal()
    assert distress_signal.part_one_search() == 5852


def test_part_two_game():
    """
    Method to test part two of day thirteen solution.
    """
    distress_signal = DistressSignal()
    assert distress_signal.part_two_search() == 24190
