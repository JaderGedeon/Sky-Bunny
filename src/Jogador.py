import pygame, time


# Classe de definição do personagem SkyBunny
class Coelho:
    def __init__(self, x, y): # Inicialização de variaveis da classe
        # Posição, Movimento, Tecla Selecionada, Pulo e Tempo Pressionado
        self.x = x
        self.y = y
        self.movimento = 16
        self.select = 0
        self.pulo = 0
        self.tempoAperta = 0
        # Array de direções do personagem
        self.direcao = [1, 2, 3, 4]
        # Boolean para personagem andando ou pulando
        self.andando = True

    # Desenha o Sprite
    def desenho(self, tela):
        pygame.draw.rect(tela, (255, 255, 255), (self.x, self.y, 16, 16))

    # Função para a habilidade de "Pulo Carregado"
    def puloCarregado(self, evento):
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    self.tempoAperta = time.time()  # Tempo em que a tecla é pressionada
                    self.andando = False  # Trava o movimento do jogador enquanto pressionada
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_SPACE:
                    tempoSolta = time.time()  # Tempo em que a tecla é liberada
                    tempoTotal = int(tempoSolta - self.tempoAperta)  # Duração em que a tecla ficou ativada

                    # Definição da distância do pulo pelo tempo de ativação da tecla
                    if 3 > tempoTotal >= 1:  # Menor pulo
                        self.pulo = 2
                    elif tempoTotal >= 3:  # Maior pulo
                        self.pulo = 3

                    # Movimentação baseada na direção selecionada
                    if self.select == 1:
                        self.y -= self.pulo*self.movimento
                    elif self.select == 2:
                        self.y += self.pulo*self.movimento
                    elif self.select == 3:
                        self.x -= self.pulo*self.movimento
                    elif self.select == 4:
                        self.x += self.pulo*self.movimento

                    # Reset do movimento do jogador pós pulo
                    self.andando = True

    # Função para a definição da movimentação basica do Personagem
    def movimentoBasico(self):
        tecla = pygame.key.get_pressed()

        if tecla[pygame.K_UP]:
            self.select = self.direcao[0]
            if self.andando is True:
                self.y -= self.movimento

        if tecla[pygame.K_DOWN]:
            self.select = self.direcao[1]
            if self.andando is True:
                self.y += self.movimento

        if tecla[pygame.K_LEFT]:
            self.select = self.direcao[2]
            if self.andando is True:
                self.x -= self.movimento

        if tecla[pygame.K_RIGHT]:
            self.select = self.direcao[3]
            if self.andando is True:
                self.x += self.movimento
