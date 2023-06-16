import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu


class Game:
    CENTER_SCREEN=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2)
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.menu = Menu('Press Any Key To Start....', self.screen, self.CENTER_SCREEN)
        self.running = False
        self.death_count = 0
        self.score = 0
        self.highest_score  = 0
        
        
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()        
        
    def run(self):
        # Game loop: events - update - draw
        self.score = 0       
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        #pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_menu(self):
        self.menu.reset(self.screen)
        if self.death_count > 0:
            messages =['Game over. Press any key to restart',f'Your score: {self.score}' , f'Highest score : {self.highest_score }', f'Total deaths: {self.death_count}']
            positions = [self.CENTER_SCREEN, (self.CENTER_SCREEN[0],self.CENTER_SCREEN[1]+50),(self.CENTER_SCREEN[0],self.CENTER_SCREEN[1]+100),(self.CENTER_SCREEN[0],self.CENTER_SCREEN[1]+150)]
            self.menu.update_message(messages,positions)
        self.menu.draw(self.screen)
        half_screen_width = SCREEN_WIDTH//2
        half_screen_height = SCREEN_HEIGHT//2
        icon = pygame.transform.scale(ICON, (80,120) )
        self.screen.blit(icon,(half_screen_width - 50,half_screen_height - 150))
        self.menu.update(self)
        
    def update_highest_score(self):
        if self.score > self.highest_score :
            self.highest_score  = self.score
   
    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True,(255,255,255)) 
        text_rect = text.get_rect() 
        text_rect.center = (1000,50) 
        self.screen.blit(text,text_rect)
            