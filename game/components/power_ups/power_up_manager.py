import random
import pygame
from game.components.power_ups.shield import Shield
from game.components.power_ups.double_shot import DoubleShot
from game.components.power_ups.speed_plus import SpeedPlus
from game.utils.constants import SPACESHIP_SHIELD

class PowerUpManager:
    MIN_TIME_POWER_UP = 5000
    MAX_TIME_POWER_UP = 10000
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(self.MIN_TIME_POWER_UP, self.MAX_TIME_POWER_UP)
        
    
    def generate_power_up(self):
        power_ups = {"shield":Shield(), "double_shot": DoubleShot() ,"speed_plus":SpeedPlus()}
        self.when_appears += random.randint(self.MIN_TIME_POWER_UP, self.MAX_TIME_POWER_UP)
        self.power_ups.append(power_ups[random.choice(list(power_ups.keys()))])
    
    def update(self, game):
        current_time = pygame.time.get_ticks()
        
        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()
        
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups) 
            if game.player.rect.colliderect(power_up) and power_up.type == "shield":
                power_up.start_time = pygame.time.get_ticks()
                game.player.power_up_type = power_up.type
                game.player.has_power_up = True
                self.duration = random.randint(3,5)
                game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                game.player.set_image((65,75), SPACESHIP_SHIELD )
                self.power_ups.remove(power_up)
            elif game.player.rect.colliderect(power_up) and power_up.type == "double_shot": 
                power_up.start_time = pygame.time.get_ticks()
                game.player.power_up_type = power_up.type
                game.player.has_power_up = True
                self.duration = random.randint(6,12)
                game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                self.power_ups.remove(power_up)
                
            elif game.player.rect.colliderect(power_up) and power_up.type == "speed_plus": 
                power_up.start_time = pygame.time.get_ticks()
                game.player.power_up_type = power_up.type
                game.player.has_power_up = True
                self.duration = random.randint(10,20)
                game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                self.power_ups.remove(power_up)    
                  
                  
    
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
            
            
    def reset(self):
        self.power_ups=[]
        now = pygame.time.get_ticks()
        self.when_appears = random.randint(now+self.MIN_TIME_POWER_UP, now +self.MAX_TIME_POWER_UP)