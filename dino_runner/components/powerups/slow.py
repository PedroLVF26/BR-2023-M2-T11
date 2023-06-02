from dino_runner.utils.constants import SLOW, SLOW_TYPE
from dino_runner.components.powerups.power_up import PowerUp


class Slow(PowerUp):
    def __init__(self):
        self.image = SLOW
        self.type = SLOW_TYPE
        super().__init__(self.image, self.type)
