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
        Вводить числа не надо (булево?) Можно посмотреть сколько сокровищ сейчас накопилось
        """
        while self.status is True:
            time.sleep(self.update_time_sec)
            if self.status is False:
                break
            self.treasure += self.treasure_update
            if self.treasure >= self.full:
                self.status = False

    def update_treasure(self):
        self.treasure = 0
        self.status = False

    def treasure_counter_thread_start(self):
        if self.status is False:
            self.status = True
            self.treasure = 0
            thread = Thread(target=self.counter, daemon=True)
            thread.run()
