import pygame

class Cenoura(pygame.sprite.Sprite):
    def __init__(self, coelho):
        pygame.sprite.Sprite.__init__(self)
        self.cor = (255, 0, 0)
        self.x = 200
        self.y = 200
        self.altura = 16
        self.largura = 16
        self.movimento = 8
        self.rangeMax = 64

        self.desenho()

        self.coelho = coelho
        self.andando = True
        self.ativo = False

        self.ativoEvento = pygame.USEREVENT + 7

    # ======================================================================================

    def desenho(self):
        self.image = pygame.Surface((self.largura, self.altura))
        self.image.fill(self.cor)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    # ======================================================================================

    def ativacaoTimer(self):
        pygame.time.set_timer(self.ativoEvento, 1000)

    # ======================================================================================

    def ativacaoEvento(self, evento):
        global coelho
        if evento.type == self.ativoEvento:
            distancia = ((self.coelho.rect.x - self.rect.x), (self.coelho.rect.y - self.rect.y))

            if - distancia[0] < self.rangeMax > distancia[0]:
                if - distancia[1] < self.rangeMax > distancia[1]:
                    self.ativo = True

    # ======================================================================================

    def movimentoBasico(self):
        global coelho

        self.andando = True

        if self.ativo is True:
            if self.coelho.morreu is True:
                self.andando = False
            if self.coelho.levouDano is False and self.andando is True:
                if self.rect.x < self.coelho.rect.x:
                    self.rect.x += self.movimento
                if self.rect.x > self.coelho.rect.x:
                    self.rect.x -= self.movimento

                if self.rect.y < self.coelho.rect.y:
                    self.rect.y += self.movimento
                if self.rect.y > self.coelho.rect.y:
                    self.rect.y -= self.movimento
            elif self.coelho.levouDano is True:
                if self.rect.x < self.coelho.rect.x:
                    self.rect.x -= self.movimento
                elif self.rect.x > self.coelho.rect.x:
                    self.rect.x += self.movimento

                if self.rect.y < self.coelho.rect.y:
                    self.rect.y -= self.movimento
                elif self.rect.y > self.coelho.rect.y:
                    self.rect.y += self.movimento