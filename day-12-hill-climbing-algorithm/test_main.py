from main import HillClimbingAlgorithm


def test_part_one_game():
    """
    Method to test part one of day twelve solution.
    """
    hill_climb = HillClimbingAlgorithm()
    assert hill_climb.part_one_search() == 504


def test_part_two_game():
    """
    Method to test part two of day twelve solution.
    """
    hill_climb = HillClimbingAlgorithm()
    assert hill_climb.part_two_search() == 500
