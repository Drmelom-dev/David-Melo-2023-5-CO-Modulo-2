import pygame
from pygame import mixer

from game.utils.constants import SHIELD_TYPE

class BulletManager:
  
  pygame.mixer.pre_init(44100, -16, 2, 512)
  mixer.init()
  explosion_fx = pygame.mixer.Sound("game/assets/Sound/explosion.wav")
  explosion_fx.set_volume(0.25)
  explosion_fx2 = pygame.mixer.Sound("game/assets/Sound/explosion2.wav")
  explosion_fx2.set_volume(0.25)
  

  def __init__(self):
    self.bullets = []
    self.enemy_bullets = []
    
  def update(self, game):
    for bullet in self.bullets:
      bullet.update(self.bullets)

      for enemy in game.enemy_manager.enemies:
        if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
            game.enemy_manager.enemies.remove(enemy)
            self.bullets.remove(bullet)
            self.explosion_fx.play()
            game.score.update()

    for bullet in self.enemy_bullets:
      bullet.update(self.enemy_bullets)
      
      if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
        self.enemy_bullets.remove(bullet)
        self.explosion_fx2.play()
        if game.player.power_up_type != SHIELD_TYPE:
          game.death_count.update()
          game.playing = False
          pygame.time.delay(1000)
          break
  
  def draw(self, screen):
    for bullet in self.enemy_bullets:
      bullet.draw(screen)
    
    for bullet in self.bullets:
      bullet.draw(screen)
      
  def add_bullet(self, bullet, n_bullets=10):
    if bullet.owner == 'player' and len(self.bullets) < n_bullets:
      self.bullets.append(bullet)
    elif bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
      self.enemy_bullets.append(bullet)
      
  def reset(self):
    self.bullets = []
    self.enemy_bullets = []
