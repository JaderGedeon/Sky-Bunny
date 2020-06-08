import pygame, time


# Classe de definição do personagem SkyBunny
class Jogador(pygame.sprite.Sprite):
    # Função de inicialização de variáveis
    def __init__(self, x, y, sprites):
        pygame.sprite.Sprite.__init__(self) # Inicialização do Sprite
        # Definição do sprite, tamanho e movimentação
        self.altura = 64
        self.largura = 64
        self.movimento = 16
        self.stunTimer = 30
        self.direcao = [1, 2, 3, 4]
        self.sprites = sprites
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

    # ======================================================================================

    # Função de desenho
    def desenho(self, x, y):
        self.image = pygame.transform.scale(self.sprites[0], (self.largura, self.altura))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # ======================================================================================

    # Função para a Movimentação do Personagem
    def movimentoBasico(self):
        # Stun
        if self.stun is False:
            self.stunTimer = 10
        if self.stun is True:
            self.stunTimer -= 1
            self.puloAtivo = False
            self.andando = False
            if self.stunTimer == 0 or self.levouDano is True:
                self.andando = True
                self.puloAtivo = True
                self.stun = False

        # Movimentação
        tecla = pygame.key.get_pressed()

        if tecla[pygame.K_UP]:
            self.select = self.direcao[0]
            self.image = pygame.transform.scale(self.sprites[0], (self.largura, self.altura))
            if self.andando is True:
                self.rect.y -= self.movimento

        if tecla[pygame.K_DOWN]:
            self.select = self.direcao[1]
            self.image = pygame.transform.scale(self.sprites[1], (self.largura, self.altura))
            if self.andando is True:
                self.rect.y += self.movimento

        if tecla[pygame.K_LEFT]:
            self.select = self.direcao[2]
            if self.andando is True:
                self.rect.x -= self.movimento

        if tecla[pygame.K_RIGHT]:
            self.select = self.direcao[3]
            if self.andando is True:
                self.rect.x += self.movimento

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
                print("Pulo = " + str(self.puloDelay))

        if evento.type == self.DashFullCD:
            if self.puloDelay == 3:
                self.puloDelay = 0
                print("Pulo resetado")

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and self.puloAtivo is True:
                self.tempoAperta = time.time()
                self.andando = False
                self.puloAtivo = True

    # ======================================================================================

    # Função para a Habilidade de Pulo
    def puloCarregado(self, evento):
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_SPACE and self.puloAtivo is True:
                tempoSolta = time.time()
                tempoTotal = int(tempoSolta - self.tempoAperta)
                print(tempoTotal)
                if tempoTotal < 1 and self.puloDelay <= 2:
                    self.pulo = 4
                    self.puloDelay += 1
                elif 3 > tempoTotal >= 1:
                    self.pulo = 6
                elif tempoTotal >= 3:
                    self.pulo = 8

                if self.select == 1:
                    self.rect.y -= self.pulo*self.movimento
                elif self.select == 2:
                    self.rect.y += self.pulo*self.movimento
                elif self.select == 3:
                    self.rect.x -= self.pulo*self.movimento
                elif self.select == 4:
                    self.rect.x += self.pulo*self.movimento

                self.andando = True
                self.pulo = 0

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
