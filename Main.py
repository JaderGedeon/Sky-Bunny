"""
Nós,

// Jader Gedeon de Oliveira Rocha
// Pedro (Dps completa teu nome...)

declaramos que

todas as respostas são fruto de nosso próprio trabalho,
não copiamos respostas de colegas externos à equipe,
não disponibilizamos nossas respostas para colegas externos à equipe e
não realizamos quaisquer outras atividades desonestas para nos beneficiar ou prejudicar outros.
"""

import pygame

from src.Elementos_Personagens import Elementos

pygame.init()

jogoAtivo = True
cor = (0, 0, 0)
x = 300
y = 300
hit = False

elementos = Elementos.Personagens(x, y)

tela = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Teste de Movimento")

elementos.coelho.dashTimer()

while jogoAtivo:
    pygame.time.delay(100)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogoAtivo = False

        elementos.coelho.dashEvento(evento)
        elementos.coelho.puloCarregado(evento)

    elementos.coelho.vida()
    elementos.coelho.movimentoBasico()
    elementos.cenoura.movimentoBasico()

    elementos.hit()

    tela.fill(cor)
    elementos.spritesGerais.draw(tela)
    pygame.display.update()

pygame.quit()