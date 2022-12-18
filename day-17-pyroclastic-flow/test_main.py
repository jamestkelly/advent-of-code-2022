from main import PyroclasticFlow


def test_part_one_search():
    """
    Method to test part one of day seventeen solution.
    """
    pyro = PyroclasticFlow()
    assert pyro.part_one_search() == 3083


def test_part_two_search():
    """
    Method to test part two of day seventeen solution.
    """
    pyro = PyroclasticFlow()
    assert pyro.part_two_search() == 1532183908048
