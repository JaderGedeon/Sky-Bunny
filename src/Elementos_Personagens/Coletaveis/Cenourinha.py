import pygame, random

class Cenourinha(pygame.sprite.Sprite):
    def __init__(self, coelho,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.cor = (241, 91, 0)
        self.x = x
        self.y = y
        self.altura = 16
        self.largura = 16
        self.coelho = coelho

        self.desenho()

    def desenho(self):
        self.image = pygame.Surface((self.largura, self.altura))
        self.image.fill(self.cor)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y