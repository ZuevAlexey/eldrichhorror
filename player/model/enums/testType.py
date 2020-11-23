from enum import Enum
from model.enums.helper import from_str


class TestType(Enum):
    LORE = 'Lore'
    COMMUNICATION = 'Communication'
    ATTENTION = "Attention"
    STRENGTH = "Strength"
    WILL = "Will"
    DECISION = "Decision"
    FIGHT = "Fight"

    @staticmethod
    def from_str(label):
        return from_str(label, TestType)
