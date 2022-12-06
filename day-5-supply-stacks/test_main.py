from main import SupplyStacks


def test_part_one_search():
    """
    Method to test part one of day five solution.
    """
    supply = SupplyStacks()
    assert supply.part_one_simulate() == "RFFFWBPNS"


def test_part_two_search():
    """
    Method to test part two of day five solution.
    """
    supply = SupplyStacks()
    assert supply.part_two_simulate() == "CQQBBJFCS"
