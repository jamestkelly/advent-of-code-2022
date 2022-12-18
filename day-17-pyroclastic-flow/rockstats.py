from dataclasses import dataclass


@dataclass
class RockStats:
    """
    Dataclass to store additional hard-coded details for the rock objects.
    """

    def __init__(self) -> None:
        """
        Initializer for class level variables.
        """
        self.stats = {
            "horizontal-line": {
                "height": 1
            },
            "cross": {
                "height": 3
            },
            "l-shape": {
                "height": 3
            },
            "vertical-line": {
                "height": 4
            },
            "block": {
                "height": 2
            }
        }
        self.max_moves = [2022, 1000000000000]
