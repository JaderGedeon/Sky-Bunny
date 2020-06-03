import pygame, math

from src.Elementos_Personagens.Tiros import Teia

class Cenourideo(pygame.sprite.Sprite):
    def __init__(self, coelho,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.cor = (0, 0, 255)
        self.x = x
        self.y = y
        self.altura = 16
        self.largura = 16
        self.movimento = 8
        self.knockback = 16
        self.angulo = 0

        self.tirosCount = 1
        self.moveCount = 0
        self.desenho()

        self.teia = Teia.Teia(coelho, self)

        self.coelho = coelho
        self.andando = False
        self.ativo = True

    def desenho(self):
        self.image = pygame.Surface((self.largura, self.altura))
        self.image.fill(self.cor)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def movimentoBasico(self):
        global coelho

        if self.tirosCount == 4:
            self.moveCount = 30
            self.andando = True
            self.ativo = False

        if self.moveCount == 0:
            self.ativo = True
            self.andando = False

        self.angulo = math.atan2((self.rect.y - self.coelho.rect.y), (self.rect.x - self.coelho.rect.x))

        if self.coelho.morreu is True:
            self.andando = False
        if self.coelho.levouDano is False and self.andando is True:
            if self.rect.x < self.coelho.rect.x:
                self.rect.x -= self.movimento*math.cos(self.angulo)
            if self.rect.x > self.coelho.rect.x:
                self.rect.x -= self.movimento*math.cos(self.angulo)

            if self.rect.y < self.coelho.rect.y:
                self.rect.y -= self.movimento*math.sin(self.angulo)
            if self.rect.y > self.coelho.rect.y:
                self.rect.y -= self.movimento*math.sin(self.angulo)
        if self.andando is True:
            self.tirosCount = 0
            self.moveCount -= 1
