from main import CalorieCounter


def test_elf_max():
    """
    Method to test part one of day one solution.
    """
    calories = CalorieCounter()
    assert calories.elf_max() == 69501


def test_greediest_elves():
    """
    Method to test part two of day one solution.
    """
    calories = CalorieCounter()
    assert calories.greediest_elves() == 202346
