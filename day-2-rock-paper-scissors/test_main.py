from main import RockPaperScissors


def test_part_one_game():
    """
    Method to test part one of day two solution.
    """
    rock_paper_scissors = RockPaperScissors()
    assert rock_paper_scissors.part_one_game() == 15337


def test_part_two_game():
    """
    Method to test part two of day two solution.
    """
    rock_paper_scissors = RockPaperScissors()
    assert rock_paper_scissors.part_two_game() == 11696
