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

import src.MapGenerator as MG
import pygame as pg
import random

pg.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
PINK = (255,218,255)
RED = (255, 0, 0)

WIDTH = 9
HEIGHT = 9

MARGIN = 0

oi = MG.MapGenerator(130,65)
oi.inicializarIlhas()
oi.popularMapa()

WINDOW_SIZE = [1366, 768]
screen = pg.display.set_mode(WINDOW_SIZE)

pg.display.set_caption("RODA MEU DEUS")

JogoAtivo = True

while JogoAtivo:
    for event in pg.event.get():  # User did something
        if event.type == pg.QUIT:  # If user clicked close
            JogoAtivo = False  # Flag that we are done so we exit this loop
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_h:
                oi.reiniciarMapa()
    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for i in range(len(oi.mapa)):
        for j in range(len(oi.mapa[0])):

            if oi.mapa[i][j].texturaDoTile == '1':
                color = GREEN
            elif oi.mapa[i][j].texturaDoTile == '0':
                color = PINK

            pg.draw.rect(screen, color, [(MARGIN + WIDTH) * j + MARGIN, (MARGIN + HEIGHT) * i + MARGIN, WIDTH, HEIGHT])

    # Go ahead and update the screen with what we've drawn.
    pg.display.flip()