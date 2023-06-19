from game.components.power_ups.power_up import PowerUp
from game.utils.constants import  SPEED_PLUS ,SPEED_PLUS_TYPE

class SpeedPlus(PowerUp):
    def __init__(self):
        super().__init__(SPEED_PLUS,SPEED_PLUS_TYPE)