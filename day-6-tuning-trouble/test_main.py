from main import TuningTrouble


def test_part_one_search():
    """
    Method to test part one of day five solution.
    """
    tuning = TuningTrouble()
    assert tuning.part_one_trace() == 1909


def test_part_two_search():
    """
    Method to test part two of day five solution.
    """
    tuning = TuningTrouble()
    assert tuning.part_two_trace() == 3380
