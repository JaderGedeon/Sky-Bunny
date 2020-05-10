"""
Nós,

// Jader Gedeon de Oliveira Rocha
// Pedro Henrique Sueiro Pereira

declaramos que

todas as respostas são fruto de nosso próprio trabalho,
não copiamos respostas de colegas externos à equipe,
não disponibilizamos nossas respostas para colegas externos à equipe e
não realizamos quaisquer outras atividades desonestas para nos beneficiar ou prejudicar outros.
"""

import src.GeradorDeMapa as MG
import pygame as pg
import sys
import random

pg.init()

oi = MG.MapGenerator(50,50)
oi.inicializarIlhas()
oi.popularMapa()
oi.texturizarMapa()

TamanhoTile = oi.texturizador.tamanhoTexturas

WINDOW_SIZE = [1280, 600]
screen = pg.display.set_mode(WINDOW_SIZE)

pg.display.set_caption("RODA MEU DEUS")

JogoAtivo = True

def Desenhar():
    oi.texturizarMapa()
    for i in range(len(oi.mapa)):
        for j in range(len(oi.mapa[0])):
            screen.blit(oi.mapa[i][j].texturaDoTile,(j*TamanhoTile,i*TamanhoTile))

font = pg.font.Font(None, 30)
clock = pg.time.Clock()

while JogoAtivo:
    for event in pg.event.get():  # User did something
        if event.type == pg.QUIT:  # If user clicked close
            JogoAtivo = False  # Flag that we are done so we exit this loop
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_h:
                oi.reiniciarMapa()
                Desenhar()
    # Set the screen background
    #screen.fill(BLACK)
    pg.display.set_caption(str(int(clock.get_fps())))
    clock.tick(60)
    pg.display.flip()