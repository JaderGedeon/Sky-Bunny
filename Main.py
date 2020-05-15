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

import src.Jogador

pygame.init()

coelho = src.Jogador.Coelho(200, 200)
jogoAtivo = True
cor = (0, 0, 0)

tela = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Teste de Movimento")

while jogoAtivo:
    pygame.time.delay(100)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogoAtivo = False
        coelho.puloCarregado(evento)

    coelho.movimentoBasico()

    tela.fill(cor)
    coelho.desenho(tela)
    pygame.display.update()

pygame.quit()