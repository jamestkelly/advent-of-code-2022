from main import CalorieCounter


def test_elf_max():
    calories = CalorieCounter()
    assert calories.elf_max() == 69501


def test_greediest_elves():
    calories = CalorieCounter()
    assert calories.greediest_elves() == 202346
