import pygame, math, random

class Charger(pygame.sprite.Sprite):
    def __init__(self, coelho, x, y,idIlha, sprites):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.coelhoX = 0
        self.coelhoY = 0
        self.altura = 43
        self.largura = 34
        self.movimento = 16
        self.knockback = 80
        self.sprites = sprites

        self.angulo = 0

        self.desenho()

        self.coelho = coelho
        self.andando = False
        self.investida = pygame.USEREVENT + 3
        self.investidaStop = pygame.USEREVENT + 4

        self.qualIlha = idIlha

    # ======================================================================================

    def desenho(self):
        self.image = pygame.transform.scale(self.sprites[1], (self.largura*3, self.altura*3))
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
                self.rect.x -= self.movimento*math.cos(self.angulo)
            if self.rect.x > self.coelhoX:
                self.rect.x -= self.movimento * math.cos(self.angulo)

            if self.rect.y < self.coelhoY:
                pygame.transform.scale(self.sprites[0], (self.largura, self.altura))
                self.rect.y -= self.movimento*math.sin(self.angulo)
            if self.rect.y > self.coelhoY:
                pygame.transform.scale(self.sprites[1], (self.largura, self.altura))
                self.rect.y -= self.movimento*math.sin(self.angulo)
