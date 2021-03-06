import pygame, math

class Cenoura(pygame.sprite.Sprite):
    def __init__(self, coelho,x,y,idIlha, sprites):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.altura = 25
        self.largura = 19
        self.movimento = 4
        self.rangeMax = 160
        self.knockback = 32
        self.angulo = 0
        self.sprites = sprites

        self.desenho()

        self.coelho = coelho
        self.andando = True
        self.ativo = False

        self.ativoEvento = pygame.USEREVENT + 7

        self.qualIlha = idIlha

    # ======================================================================================

    def desenho(self):
        self.image = pygame.transform.scale(self.sprites[1], (self.largura*2, self.altura*2))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    # ======================================================================================

    def ativacaoTimer(self):
        pygame.time.set_timer(self.ativoEvento, 1000)

    # ======================================================================================

    def ativacaoEvento(self, evento):
        global coelho
        if evento.type == self.ativoEvento and self.ativo == False:

            distancia = ((self.coelho.rect.x - self.rect.x), (self.coelho.rect.y - self.rect.y))

            if - distancia[0] < self.rangeMax > distancia[0]:
                if - distancia[1] < self.rangeMax > distancia[1]:
                    self.ativo = True
                    self.cor = (255, 0, 0)
                    self.desenho()

    # ======================================================================================

    def movimentoBasico(self):
        global coelho

        self.angulo = math.atan2((self.rect.y - self.coelho.rect.y), (self.rect.x - self.coelho.rect.x))

        self.andando = True

        if self.ativo is True:
            if self.coelho.morreu is True:
                self.andando = False
            if self.coelho.levouDano is False and self.andando is True:
                if self.rect.x < self.coelho.rect.x:
                    self.rect.x -= self.movimento*math.cos(self.angulo)
                if self.rect.x > self.coelho.rect.x:
                    self.rect.x -= self.movimento*math.cos(self.angulo)

                if self.rect.y < self.coelho.rect.y:
                    self.rect.y -= self.movimento*math.sin(self.angulo)
                    self.image = pygame.transform.scale(self.sprites[1], (self.largura * 2, self.altura * 2))
                if self.rect.y > self.coelho.rect.y:
                    self.rect.y -= self.movimento*math.sin(self.angulo)
                    self.image = pygame.transform.scale(self.sprites[0], (self.largura * 2, self.altura * 2))
