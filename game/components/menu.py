import pygame
from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu:
    HALF_SCREEN_WIDTH = SCREEN_WIDTH//2
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT//2
    
    def __init__(self, message, screen,position):
        screen.fill((255,255,255))
        self.font = pygame.font.Font(FONT_STYLE, 30) 
        self.text = self.font.render(message, True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (position)
        self.menu_scores=False
     
        
    
    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)
        
    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.playing = False
            elif event.type == pygame.KEYDOWN:
                game.run()    
        
        
            
    
    def draw(self, screen):
        if self.menu_scores == False:
            screen.blit(self.text, self.text_rect)
        else:
            for text, rect in zip(self.texts, self.text_rects):
                screen.blit(text, rect)   
        
    
    def reset(self, screen):
        screen.fill((255,255,255))
        
    def update_message(self, messages,positions):
        self.texts = []
        self.text_rects = []
        for message,position in zip(messages,positions):
            text = self.font.render(message, True , (0,0,0)) 
            text_rect = text.get_rect()
            text_rect.center = (position) 
            self.texts.append(text)
            self.text_rects.append(text_rect)  
            self.menu_scores=True  