import time
from threading import Thread


class TreasureCounter:
    def __init__(self):
        self.status = False
        self.full = 2400
        self.update_time_sec = 6000
        self.treasure = 0
        self.treasure_update = 30

    def counter(self):
        """Сокровища обители - накапливаются 30 единиц в час, кап 2400. Когда забираешь они сбрасываются.
Вводить числа не надо (булево?) Можно посмотреть сколько сокровищ сейчас накопилось"""
        while self.status is True:
            time.sleep(self.update_time_sec)
            self.treasure += self.treasure_update

    def update_treasure(self):
        self.treasure = 0

    def treasure_counter_thread_start(self):
        thread = Thread(target=self.counter)
        thread.run()
