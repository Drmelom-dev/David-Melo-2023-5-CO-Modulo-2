from game.components.power_ups.power_up import PowerUp
from game.utils.constants import  DOUBLE_SHOT ,DOUBLE_SHOT_TYPE

class DoubleShot(PowerUp):
    def __init__(self):
        super().__init__(DOUBLE_SHOT,DOUBLE_SHOT_TYPE)