from enum import Enum
from model.enums.helper import from_str


class Location(Enum):
    CITY = 'City'
    SEA = 'Sea'
    WILDERNESS = "Wilderness"
    ARKHAM = "Arkham"
    SAN_FRANCISCO = "San Francisco"
    BUENOS_AIRES = "Buenos Aires"
    LONDON = "London"
    ROME = "Rome"
    ISTANBUL = "Istanbul"
    ZANHAE = "Zanhae"
    TOKYO = "Tokyo"
    SYDNEY = "Sydney"
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
