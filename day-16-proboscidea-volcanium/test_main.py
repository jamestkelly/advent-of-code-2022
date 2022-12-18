from main import ProboscideaVolcanium


def test_part_one_search():
    """
    Method to test part one of day sixteen solution.
    """
    proboscidea = ProboscideaVolcanium()
    assert proboscidea.part_one_search() == 2087


def test_part_two_search():
    """
    Method to test part two of day sixteen solution.
    """
    proboscidea = ProboscideaVolcanium()
    assert proboscidea.part_two_search() == 2591
