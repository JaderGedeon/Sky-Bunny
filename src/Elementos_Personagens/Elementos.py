import pygame

from src.Elementos_Personagens import Jogador
from src.Elementos_Personagens.Inimigos import Cenoura

class Personagens:
    def __init__(self, x, y):
        self.spritesGerais = pygame.sprite.Group()
        self.inimigosSprite = pygame.sprite.Group()

        self.coelho = Jogador.Jogador(x, y)
        self.spritesGerais.add(self.coelho)

        self.cenoura = Cenoura.Cenoura(self.coelho)
        self.spritesGerais.add(self.cenoura)
        self.inimigosSprite.add(self.cenoura)


    def hit(self):
        hit = pygame.sprite.spritecollide(self.coelho, self.inimigosSprite, False)
        self.coelho.levouDano = False
        if hit:
            self.coelho.levouDano = True