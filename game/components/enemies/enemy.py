import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1, SCREEN_HEIGHT, SCREEN_WIDTH, ENEMY_2
from game.components.bullets.bullet import Bullet
class Enemy(Sprite):
    ENEMY_WIDTH = 40
    ENEMY_HEIGHT = 60
    X_POS_LIST = [x for x in range(50, 1001, 50)]
    Y_POS = 20
    SPEED_X = 5
    SEPEED_Y = 4
    MOV_X = {0:'left',1:'right'}
    ENEMIES = {1:ENEMY_1,2:ENEMY_2}
    def __init__(self, image = 1, speed_x = SPEED_X, speed_y = SEPEED_Y, move_x_for = [30,100]):
        self.image = pygame.transform.scale(self.ENEMIES[image],(self.ENEMY_WIDTH, self.ENEMY_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS_LIST[random.randint(0,10)]
        self.rect.y = self.Y_POS
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.movement_x = self.MOV_X[random.randint(0,1)]
        self.move_x_for = random.randint(move_x_for[0],move_x_for[1])
        self.index = 0
        self.type = 'enemy'
        self.shooting_time = random.randint(30,50)
        
        
    def update(self, ships, game):
        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager)
        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
            self.change_movement_x()
        else:
            self.rect.x += self.speed_x 
            self.change_movement_x() 
        if self.rect.y >= SCREEN_HEIGHT :
            ships.remove(self)
            
    
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))
        
            
    def change_movement_x(self):
        self.index += 1
        if(self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.ENEMY_WIDTH):
            self.movement_x = 'left'
            self.index = 0 
        elif(self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10):
            self.movement_x =  'right'
            self.index = 0  
    
    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks() 
        if self.shooting_time <= current_time:
            bullet = Bullet(self) 
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(30,50)     
   
            