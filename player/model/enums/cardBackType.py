from enum import Enum
from model.enums.helper import from_str


class CardBackType(Enum):
    COMMON = 'Common'
    AMERICAN = 'American'
    EUROPEAN = "European"
    ASIAN = "Asian"
    EXPEDITION = "Expedition"
    OTHER_WORLD = "OtherWorld"

    @staticmethod
    def from_str(label):
        return from_str(label, CardBackType)
