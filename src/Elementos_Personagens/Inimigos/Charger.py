import pygame, math, random

class Charger(pygame.sprite.Sprite):
    def __init__(self, coelho, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.cor = (0, 255, 0)
        self.x = x
        self.y = y
        self.coelhoX = 0
        self.coelhoY = 0
        self.altura = 24
        self.largura = 24
        self.movimento = 16
        self.knockback = 64

        self.direcao = [1, 2, 3, 4]
        self.selectX = 0
        self.selectY = 0

        self.angulo = 0

        self.desenho()

        self.coelho = coelho
        self.andando = False
        self.investida = pygame.USEREVENT + 3
        self.investidaStop = pygame.USEREVENT + 4

    # ======================================================================================

    def desenho(self):
        self.image = pygame.Surface((self.largura, self.altura))
        self.image.fill(self.cor)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    # ======================================================================================

    def investidaTimer(self):
        pygame.time.set_timer(self.investida, 3000)
        pygame.time.set_timer(self.investidaStop, 1000)

    # ======================================================================================

    def investidaEvento(self, evento):
        if evento.type == self.investida:
            if self.coelho.morreu is False:
                self.andando = True
        if evento.type == self.investidaStop and self.andando is True:
            self.andando = False

    # ======================================================================================

    def movimentoBasico(self):
        global coelho
        if self.andando is False:
            self.coelhoX = self.coelho.rect.x
            self.coelhoY = self.coelho.rect.y
            self.angulo = math.atan2((self.rect.y - self.coelhoY), (self.rect.x - self.coelhoX))

        if self.coelho.morreu is True:
            self.andando = False
        if self.andando is True:
            if self.rect.x < self.coelhoX:
                self.selectX = self.direcao[0]
                self.rect.x -= self.movimento*math.cos(self.angulo)
            if self.rect.x > self.coelhoX:
                self.selectX = self.direcao[1]
                self.rect.x -= self.movimento * math.cos(self.angulo)

            if self.rect.y < self.coelhoY:
                self.selectY = self.direcao[2]
                self.rect.y -= self.movimento*math.sin(self.angulo)
            if self.rect.y > self.coelhoY:
                self.selectY = self.direcao[3]
                self.rect.y -= self.movimento*math.sin(self.angulo)
