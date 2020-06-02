import pygame, math

class Teia(pygame.sprite.Sprite):
    def __init__(self, coelho, cenourideo):
        pygame.sprite.Sprite.__init__(self)
        self.cor = (0, 0, 150)
        self.largura = 8
        self.altura = 8
        self.movimento = 14
        self.rangeMax = 100
        self.angulo = 0

        self.cenourideo = cenourideo
        self.coelho = coelho

        self.desenho()

        self.resetar = True
        self.atirar = True

        self.duracao = pygame.USEREVENT + 5
        self.tiroCD = pygame.USEREVENT + 6

    def desenho(self):
        self.image = pygame.Surface((self.largura, self.altura))
        self.image.fill(self.cor)
        self.rect = self.image.get_rect()
        self.rect.x = self.cenourideo.rect.x + self.largura/2
        self.rect.y = self.cenourideo.rect.y + self.altura/2

    def tiroTimer(self):
        pygame.time.set_timer(self.duracao, 1400)

    def tiroDistanciaEvento(self, evento):
        if evento.type == self.duracao and self.resetar is False:
            self.resetar = True


    def movimentoBasico(self):
        global coelho

        if self.cenourideo.ativo is True:
            if self.atirar is True:
                self.angulo = math.atan2((self.rect.y - self.coelho.rect.y), (self.rect.x - self.coelho.rect.x))
                self.atirar = False
                self.resetar = False

            if self.resetar is False:
                if self.rect.x < self.coelho.rect.x:
                    self.rect.x -= self.movimento * math.cos(self.angulo)
                if self.rect.x > self.coelho.rect.x:
                    self.rect.x -= self.movimento * math.cos(self.angulo)

                if self.rect.y < self.coelho.rect.y:
                    self.rect.y -= self.movimento * math.sin(self.angulo)
                if self.rect.y > self.coelho.rect.y:
                    self.rect.y -= self.movimento * math.sin(self.angulo)
        if self.resetar is True:
            self.rect.x = self.cenourideo.rect.x + self.largura / 2
            self.rect.y = self.cenourideo.rect.y + self.altura / 2
            self.atirar = True
            self.cenourideo.tirosCount += 1