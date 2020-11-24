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

    @staticmethod
    def from_str(label):
        return from_str(label, Location)
