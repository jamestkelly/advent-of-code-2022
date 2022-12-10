from main import DeviceSpace


def test_part_one_search():
    """
    Method to test part one of day seven solution.
    """
    device = DeviceSpace()
    assert device.part_one_search() == 1581595


def test_part_two_search():
    """
    Method to test part two of day seven solution.
    """
    device = DeviceSpace()
    assert device.part_two_search() == 1544176
