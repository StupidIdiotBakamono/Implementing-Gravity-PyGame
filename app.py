import pygame
import pygame.display
import pygame.sprite
from pygame.locals import *



class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y
        self.width = 100
        self.height = 100

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((80, 80, 80))

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.gravity = 0
        self.speed = 10
    
    def update(self):
        # Main Gravity
        if self.rect.y == height - self.width:
            self.gravity = -35

        self.gravity += 1
        self.rect.y += self.gravity

        # Movement
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_a]:
            self.rect.x -= self.speed
        if keys_pressed[K_d]:
            self.rect.x += self.speed

        # Changing Positions
        if self.rect.x < 0 - self.width:
            self.rect.x = width + self.width
        if self.rect.x > width + self.width:
            self.rect.x = 0 - self.width
        


width, height = 1500, 750
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Implementing Gravity")



clock = pygame.time.Clock()
FPS = 60


player = Player(width/2 - 100/2, height - 100)
player_group = pygame.sprite.Group()
player_group.add(player)



while 1:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Draw
    display.fill((50, 50, 50))
    player_group.draw(display)
    player_group.update()

    pygame.display.update()