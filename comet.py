import pygame

# definir une classe pour gérer la comet
class Comet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Assets/comet.png')
        self.rect = self.image.get_rect()