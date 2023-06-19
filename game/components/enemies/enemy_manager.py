import random
import pygame
from game.components.enemies.enemy import Enemy


class EnemyManager:
  def __init__(self):
    self.enemies = []
    self.enemy_spawn_timer = 0
    
  def update(self, game):
    current_time = pygame.time.get_ticks()
    if current_time - self.enemy_spawn_timer >= 2000:  # Genera nuevos enemigos cada 2 segundos
            self.add_enemy()
            self.enemy_spawn_timer = current_time

    for enemy in self.enemies:
      enemy.update(self.enemies, game)
  
  def draw(self, screen):
    for enemy in self.enemies:
      enemy.draw(screen)
      
  def add_enemy(self):
    enemy_type = random.randint(1,2)
    if enemy_type == 1:
      enemy = Enemy()
    else:
      x_speed = 5
      y_speed = 2
      move_x_for = [1000, 1200]
      enemy = Enemy(enemy_type, x_speed, y_speed, move_x_for)
      
    self.enemies.append(enemy)
      
  def reset(self):
    self.enemies = []
    