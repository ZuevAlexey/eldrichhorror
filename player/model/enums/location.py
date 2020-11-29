from enum import Enum
from model.enums.helper import from_str


class Location(Enum):
    # Common and Research
    CITY = 'City'
    SEA = 'Sea'
    WILDERNESS = "Wilderness"
    # American
    ARKHAM = "Arkham"
    SAN_FRANCISCO = "San Francisco"
    BUENOS_AIRES = "Buenos Aires"
    # European
    LONDON = "London"
    ROME = "Rome"
    ISTANBUL = "Istanbul"
    # Asian
    ZANHAE = "Zanhae"
    TOKYO = "Tokyo"
    SYDNEY = "Sydney"
    # Expedition
    HEART_OF_AFRICA = "Heart of Africa"
    HIMALAYAS = "Himalayas"
    TUNGUSKA = "Tunguska"
    ANTARCTICA = "Antarctica"
    PYRAMIDS = "Pyramids"
    AMAZON = "Amazon"

    @staticmethod
    def from_str(label):
        if label is None:
            return None

        return from_str(label, Location)
