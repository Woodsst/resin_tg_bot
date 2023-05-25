import time
from log import logger


class User:

    def __init__(self, chat_id):
        self.id = chat_id
        self.status = True
        self.checkpoints = [40, 80, 120, 140, 160]
        self.full = self.checkpoints[-1]
        self.counter_update_time_sec = 360

    def resin_counter(self, resin: int):
        while self.status is True:
            for i in self.checkpoints:
                if resin < i:
                    resin += 1
                    logger.info(f"{self.id} resin update {resin}")
                    time.sleep(self.counter_update_time_sec)
                    break
                if resin == i:
                    yield i
                if resin == self.full:
                    yield self.full
                    resin = 0
                    self.status = False
                    break
