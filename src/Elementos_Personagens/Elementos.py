import pygame, math, random

from src.Elementos_Personagens import Jogador
from src.Elementos_Personagens.Inimigos import Cenoura, Charger, Cenourideo
from src.Elementos_Personagens.Tiros import Teia


class Personagens:
    def __init__(self, x, y):
        self.spritesGerais = pygame.sprite.Group()
        self.inimigosSprite = pygame.sprite.Group()

        self.cenouras = pygame.sprite.Group()
        self.chargers = pygame.sprite.Group()
        self.cenourideos = pygame.sprite.Group()

        self.tirosSprite = pygame.sprite.Group()

        self.jogadorGroup(x, y)
        #self.cenourasGroup()
        #self.chargersGroup()
        #self.cenourideoGroup()

        self.spritesGerais.add(self.inimigosSprite)
        self.spritesGerais.add(self.tirosSprite)
        self.spritesGerais.add(self.coelho)

    def jogadorGroup(self, x, y):
        self.coelho = Jogador.Jogador(x, y)

    def cenourasGroup(self):
        for charger in range(1):
            self.cenoura = Cenoura.Cenoura(self.coelho)
            self.cenouras.add(self.cenoura)
            self.inimigosSprite.add(self.cenouras)

    def chargersGroup(self,x,y):
        #for charger in range(100):
            self.charger = Charger.Charger(self.coelho,x,y)
            self.chargers.add(self.charger)
            self.inimigosSprite.add(self.chargers)
            self.spritesGerais.add(self.inimigosSprite)

    def cenourideoGroup(self):
        for charger in range(1):
            self.cenourideo = Cenourideo.Cenourideo(self.coelho)
            self.cenourideos.add(self.cenourideo)
            self.inimigosSprite.add(self.cenourideos)

            self.teia = Teia.Teia(self.coelho, self.cenourideo)
            self.tirosSprite.add(self.teia)

    def hit(self):
        self.coelho.levouDano = False
        self.coelho.dano = 1

        hit = pygame.sprite.spritecollide(self.coelho, self.inimigosSprite, False)
        if hit:
            self.coelho.levouDano = True

        hirCharger = pygame.sprite.spritecollide(self.coelho, self.chargers, False)
        if hirCharger:
            self.coelho.rect.x -= self.charger.knockback * math.cos(self.charger.angulo)
            self.coelho.rect.y -= self.charger.knockback * math.sin(self.charger.angulo)

        hitTeia = pygame.sprite.spritecollide(self.coelho, self.tirosSprite, False)
        if hitTeia:
            self.coelho.stun = True
            self.cenourideo.tirosCount = 4