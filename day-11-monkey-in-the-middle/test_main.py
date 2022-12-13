from main import MonkeyBusiness


def test_part_one_game():
    """
    Method to test part one of day eleven solution.
    """
    monkey_business = MonkeyBusiness()
    assert monkey_business.part_one_search() == 99840


def test_part_two_game():
    """
    Method to test part two of day eleven solution.
    """
    monkey_business = MonkeyBusiness()
    assert monkey_business.part_one_search() == 99840
    assert monkey_business.part_two_search() == 20683044837

