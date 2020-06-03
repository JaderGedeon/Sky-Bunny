import pygame, math, random

from src.Elementos_Personagens import Jogador
from src.Elementos_Personagens.Inimigos import Cenoura, Charger, Cenourideo
from src.Elementos_Personagens.Coletaveis import Cenourinha
from src.Elementos_Personagens.Tiros import Teia


class Personagens:
    def __init__(self, x, y):
        self.spritesGerais = pygame.sprite.Group()
        self.inimigosSprite = pygame.sprite.Group()
        self.coletaveis = pygame.sprite.Group()

        self.cenouras = pygame.sprite.Group()
        self.chargers = pygame.sprite.Group()
        self.cenourideos = pygame.sprite.Group()
        self.cenourinhas = pygame.sprite.Group()

        self.tirosSprite = pygame.sprite.Group()

        self.jogadorGroup(x, y)
        #self.cenourasGroup()
        #self.chargersGroup()
        #self.cenourideoGroup()

        self.spritesGerais.add(self.inimigosSprite)
        self.spritesGerais.add(self.tirosSprite)
        self.spritesGerais.add(self.coelho)
        self.spritesGerais.add(self.cenourinhas)

    def jogadorGroup(self, x, y):
        self.coelho = Jogador.Jogador(x, y)

    def cenourasGroup(self,x,y,idIlha):
        #for charger in range(1):
            self.cenoura = Cenoura.Cenoura(self.coelho,x,y,idIlha)
            self.cenouras.add(self.cenoura)
            self.inimigosSprite.add(self.cenouras)
            self.spritesGerais.add(self.inimigosSprite)

    def chargersGroup(self,x,y,idIlha):
        #for charger in range(100):
            self.charger = Charger.Charger(self.coelho,x,y,idIlha)
            self.chargers.add(self.charger)
            self.inimigosSprite.add(self.chargers)
            self.spritesGerais.add(self.inimigosSprite)

    def cenourideoGroup(self,x,y,idIlha):
        #for charger in range(1):
            self.cenourideo = Cenourideo.Cenourideo(self.coelho,x,y,idIlha)
            self.cenourideos.add(self.cenourideo)
            self.inimigosSprite.add(self.cenourideos)
            self.spritesGerais.add(self.inimigosSprite)

            self.teia = Teia.Teia(self.coelho, self.cenourideo)
            self.tirosSprite.add(self.teia)

    def coletavelGroup(self,x,y):
        #for coletavel in range(5):
            self.cenourinha = Cenourinha.Cenourinha(self.coelho,x,y)
            self.cenourinhas.add(self.cenourinha)
            #self.coletaveis.add(self.cenoura)

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

        hitCenoura = pygame.sprite.spritecollide(self.coelho, self.cenouras, False)
        if hitCenoura:
            self.coelho.rect.x -= self.cenoura.knockback * math.cos(self.cenoura.angulo)
            self.coelho.rect.y -= self.cenoura.knockback * math.sin(self.cenoura.angulo)

        hitCenourideo = pygame.sprite.spritecollide(self.coelho, self.cenourideos, False)
        if hitCenourideo:
            self.coelho.rect.x -= self.cenourideo.knockback * math.cos(self.cenourideo.angulo)
            self.coelho.rect.y -= self.cenourideo.knockback * math.sin(self.cenourideo.angulo)

        hitTeia = pygame.sprite.spritecollide(self.coelho, self.tirosSprite, False)
        if hitTeia:
            self.coelho.stun = True
            self.cenourideo.tirosCount = 4

        #coleta = pygame.sprite.spritecollide(self.coelho, self.cenourinhas, True)