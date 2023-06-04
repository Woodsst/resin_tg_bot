from bot.parametric_converter.converter_counter import ConverterCounter
from bot.resident_treasure.treasure_counter import TreasureCounter
from bot.resin.resin_counter import ResinCounter

users = {}


class User:
    def __init__(self, chat_id: int, username: str):
        self.name = username
        self.id = chat_id
        self.treasure_counter = TreasureCounter()
        self.converter_counter = ConverterCounter()
        self.resin_counter = ResinCounter()
