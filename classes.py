import pygame
import random

FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 1024
HIGHT = 768

class Canon:
    def __init__(self):
        self.image = pygame.Surface((20, 20))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HIGHT
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        
    

        



class GameWindow:
    def __init__(self):
        pygame.init()
        self.size = (WIDTH, HIGHT)
        self.title = "GAME"
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)
        self.screen.fill(WHITE)

    def main_loop(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            
            pygame.display.flip()
            clock.tick(FPS)


def main():
    window = GameWindow()
    canon = Canon()
    window.main_loop()
    


main()



