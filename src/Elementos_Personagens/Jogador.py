import pygame, time

class Hitbox(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.altura = 20
        self.largura = 32
        self.movimento = 16

        self.image = pygame.Surface((self.largura, self.altura), pygame.SRCALPHA)
        self.image.fill((255,255,255, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y + 12


# Classe de definição do personagem SkyBunny
class Jogador(pygame.sprite.Sprite):
    # Função de inicialização de variáveis
    def __init__(self, x, y, sprites, hitbox):
        pygame.sprite.Sprite.__init__(self) # Inicialização do Sprite
        # Definição do sprite, tamanho e movimentação
        self.altura = 31
        self.largura = 17
        self.movimento = 14
        self.stunTimer = 30
        self.inv = 0
        self.direcao = [1, 2, 3, 4]
        self.sprites = sprites
        self.hitbox = hitbox
        # Chama a função para desenhar o Sprite
        self.desenho(x, y)
        # Definições para o Pulo
        self.select = 0
        self.pulo = 0
        self.puloDelay = 0
        # Definições para o a vida
        self.hp = 3
        self.vidas = 3
        # Booleanas de movimento, detecção de dano e morte
        self.andando = True
        self.levouDano = False
        self.morreu = False
        self.stun = False
        self.puloAtivo = True
        # Variaveis para eventos personalizados
        self.DashCD = pygame.USEREVENT + 1
        self.DashFullCD = pygame.USEREVENT + 2
        # Ilha em que o coelho está
        self.qualIlha = -1
        self.tempoTotal = 0
        self.tempoAperta = 0
        self.tempoAmostral = 0
        self.tempoConta = 0
        self.cont = False
        self.prepPulo = False

    # ======================================================================================

    # Função de desenho
    def desenho(self, x, y):
        self.image = pygame.transform.scale(self.sprites[0], (self.largura * 2, self.altura * 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # ======================================================================================

    # Função para a Movimentação do Personagem
    def movimentoBasico(self):
        # Stun
        if self.stun is False:
            self.stunTimer = 30
        if self.stun is True and self.inv < 0:
            self.stunTimer -= 2
            self.puloAtivo = False
            self.andando = False
            if self.stunTimer <= 0 or self.levouDano is True:
                self.andando = True
                self.puloAtivo = True
                self.stun = False



        # Movimentação
        tecla = pygame.key.get_pressed()

        if tecla[pygame.K_UP]:
            self.select = self.direcao[0]
            self.image = pygame.transform.scale(self.sprites[0], (self.largura * 2, self.altura * 2))
            if self.andando is True:
                self.rect.y -= self.movimento
                self.hitbox.rect.y -= self.movimento

        if tecla[pygame.K_DOWN]:
            self.select = self.direcao[1]
            self.image = pygame.transform.scale(self.sprites[1], (self.largura * 2, self.altura * 2))
            if self.andando is True:
                self.rect.y += self.movimento
                self.hitbox.rect.y += self.movimento

        if tecla[pygame.K_LEFT]:
            self.select = self.direcao[2]
            self.image = pygame.transform.scale(self.sprites[3], (self.largura * 2, self.altura * 2))
            if self.andando is True:
                self.rect.x -= self.movimento
                self.hitbox.rect.x -= self.movimento

        if tecla[pygame.K_RIGHT]:
            self.select = self.direcao[3]
            self.image = pygame.transform.scale(self.sprites[2], (self.largura * 2, self.altura * 2))
            if self.andando is True:
                self.rect.x += self.movimento
                self.hitbox.rect.x += self.movimento

    # ======================================================================================

    # Função para o Cool Down da Habilidade de Dahs
    def dashTimer(self):
        pygame.time.set_timer(self.DashCD, 4000)
        pygame.time.set_timer(self.DashFullCD, 6000)

    # Função para a Habilidade de Dash
    def dashEvento(self, evento):
        if evento.type == self.DashCD:
            if 3 > self.puloDelay >= 1:
                self.puloDelay -= 1


        if evento.type == self.DashFullCD:
            if self.puloDelay == 3:
                self.puloDelay = 0


        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and self.puloAtivo is True:
                self.tempoAperta = time.time()
                self.andando = False
                self.puloAtivo = True
                self.prepPulo = True
                if self.cont == False:
                    self.cont = True
                    self.tempoConta = time.time()
                self.tempoAmostral = int(self.tempoAperta-self.tempoConta)


    # ======================================================================================

    # Função para a Habilidade de Pulo
    def puloCarregado(self, evento):
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_SPACE and self.puloAtivo is True:
                tempoSolta = time.time()
                self.tempoTotal = int(tempoSolta - self.tempoAperta)

                if self.tempoTotal < 1 and self.puloDelay <= 2:
                    self.pulo = 1
                elif 2 > self.tempoTotal >= 1:
                    self.pulo = 2
                elif 3 > self.tempoTotal >= 2:
                    self.pulo = 3
                elif 4 > self.tempoTotal >= 3:
                    self.pulo = 4
                elif self.tempoTotal >= 4:
                    self.pulo = 5

                if self.select == 1:
                    self.rect.y -= self.pulo*self.movimento*5
                    self.hitbox.rect.y -= self.pulo * self.movimento
                elif self.select == 2:
                    self.rect.y += self.pulo*self.movimento*5
                    self.hitbox.rect.y += self.pulo * self.movimento
                elif self.select == 3:
                    self.rect.x -= self.pulo*self.movimento*5
                    self.hitbox.rect.x -= self.pulo * self.movimento
                elif self.select == 4:
                    self.rect.x += self.pulo*self.movimento*5
                    self.hitbox.rect.x += self.pulo * self.movimento

                self.tempoTotal = 0
                self.andando = True
                self.pulo = 0
                self.cont = False
                self.prepPulo = False

    # ======================================================================================

    # Função para definição do HP e o sistema de Vidas
    def vida(self):
        if self.levouDano is True:
            self.hp -= 1

        if self.hp == 0:
            self.vidas -= 1
            self.hp = 3

        if self.vidas == 0:
            self.morreu = True