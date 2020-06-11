import pygame, random

class Cenourinha(pygame.sprite.Sprite):
    def __init__(self, coelho,x,y, sprite):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.altura = 25
        self.largura = 19
        self.coelho = coelho
        self.sprite = sprite

        self.desenho()

    def desenho(self):
        self.image = pygame.transform.scale(self.sprite, (self.largura*2, self.altura*2))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y