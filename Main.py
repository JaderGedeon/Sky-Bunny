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

from src.Elementos_Personagens import Elementos
import src.GeradorDeMapa as MG
import src.Menus as MN
import src.Pontuador as PN
import pygame as pg
import sys
import random

pg.init()

oi = MG.MapGenerator(85,120)
oi.inicializarIlhas()
oi.popularMapa()
oi.texturizarMapa()

pontuador = PN.Pontuador()
pontuador.lerPontuação()

TamanhoTile = oi.texturizador.tamanhoTexturas

UI = MN.Menus()

WINDOW_SIZE = [1280, 720]
screen = pg.display.set_mode(WINDOW_SIZE)

pg.display.set_caption("RODA MEU DEUS")

JogoAtivo = True

def Desenhar():
    oi.texturizarMapa()

font = pg.font.Font("fontes/Retro Gaming.ttf", 16*4)
clock = pg.time.Clock()

foi = False
tempo = 0
tempoInicial = 0
tempoDiferencial = 0

JogoAtivo = True

#MENUS
MenuPrincipal = True
MenuOpções = False
MenuCréditos = False
MenuAddRank = False
MenuRank = False

EmJogo = False

contadorIndexMenu = 1
contadorIndexMenuOpções = 1

contadorIndexMenuAddRank = 1
contadorIndexLetraAddRank = 1

jogadorNome = ["A","A","A"]
pontuacao = 1000

diferençatempo = 0

#Música
volume = 0.5

pg.mixer.init()
pg.mixer.music.load('musica/musicaPrincipal.mp3')
pg.mixer.music.play(loops=-1, start=0.0)
pg.mixer.music.set_volume(volume)

# ==================================================

x = 300
y = 300
hit = False

elementos = Elementos.Personagens(x, y)

elementos.coelho.dashTimer()

# ==================================================

while JogoAtivo:
    for event in pg.event.get():  # User did something

        if MenuPrincipal:
            # Desenha o menu
            UI.menuPrincipal(screen, contadorIndexMenu)

            if event.type == pg.KEYDOWN:
                # Baixo direita
                if event.key == pg.K_DOWN or event.key == pg.K_RIGHT:
                    contadorIndexMenu += 1
                    if contadorIndexMenu > 5:
                        contadorIndexMenu = 1
                # Cima esquerda
                if event.key == pg.K_UP or event.key == pg.K_LEFT:
                    contadorIndexMenu -= 1
                    if contadorIndexMenu < 1:
                        contadorIndexMenu = 5

                # Escolha de menu
                if event.key == pg.K_SPACE:
                    MenuPrincipal = False

                    #Inicia o jogo
                    if contadorIndexMenu == 1:
                        screen.fill((0, 0, 0))
                        oi.reiniciarMapa()
                        Desenhar()
                        foi = True
                        tempoInicial = pg.time.get_ticks()
                        EmJogo = True

                    # Load
                    if contadorIndexMenu == 2:
                        screen.fill((0, 0, 0))
                        pass

                    # Options
                    if contadorIndexMenu == 3:
                        diferençatempo = tempo
                        MenuOpções = True

                    # Rank
                    if contadorIndexMenu == 4:
                        diferençatempo = tempo
                        MenuRank = True

                    #Sai do jogo
                    if contadorIndexMenu == 5:
                        JogoAtivo = False

        if MenuOpções:
            UI.menuOpções(screen, contadorIndexMenuOpções, volume)

            if event.type == pg.KEYDOWN:
                # Baixo
                if event.key == pg.K_DOWN:
                    contadorIndexMenuOpções += 1
                    if contadorIndexMenuOpções > 3:
                        contadorIndexMenuOpções = 1
                # Cima
                if event.key == pg.K_UP:
                    contadorIndexMenuOpções -= 1
                    if contadorIndexMenuOpções < 1:
                        contadorIndexMenuOpções = 3

                # SOM
                if contadorIndexMenuOpções == 2:
                    print(volume)
                    if event.key == pg.K_RIGHT:
                        if volume < 0.9:
                            volume += 0.1
                            pg.mixer.music.set_volume(volume)
                    if event.key == pg.K_LEFT:
                        if volume > 0.1:
                            volume -= 0.1
                            pg.mixer.music.set_volume(volume)



                if event.key == pg.K_SPACE and diferençatempo != tempo and contadorIndexMenuOpções != 2:
                    MenuOpções = False

                    #Volta
                    if contadorIndexMenuOpções == 1:
                        MenuPrincipal = True

                    # Créditos
                    if contadorIndexMenuOpções == 3:
                        diferençatempo = tempo
                        MenuCréditos = True

        if MenuCréditos:
            UI.menuCréditos(screen)

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and diferençatempo != tempo:
                    MenuCréditos = False
                    MenuOpções = True
                    
        if MenuAddRank:
            UI.menuAddRank(screen, contadorIndexMenuAddRank+2, contadorIndexLetraAddRank, jogadorNome, pontuacao)

            if event.type == pg.KEYDOWN:
                # Baixo
                if event.key == pg.K_RIGHT:
                    if contadorIndexMenuAddRank == 1:
                        if contadorIndexLetraAddRank < 3:
                            contadorIndexLetraAddRank += 1
                        elif contadorIndexLetraAddRank == 3:
                            contadorIndexMenuAddRank += 1

                    elif contadorIndexMenuAddRank < 3:
                        contadorIndexMenuAddRank += 1
                # Cima
                if event.key == pg.K_LEFT:

                    if contadorIndexMenuAddRank == 1:
                        if contadorIndexLetraAddRank > 1:
                            contadorIndexLetraAddRank -= 1
                    else:
                        contadorIndexMenuAddRank -= 1

                if contadorIndexMenuAddRank == 1:
                    if event.key == pg.K_UP:
                        jogadorNome[contadorIndexLetraAddRank-1] = UI.SelecionarLetras(jogadorNome[contadorIndexLetraAddRank-1],-1)
                    if event.key == pg.K_DOWN:
                        jogadorNome[contadorIndexLetraAddRank-1] = UI.SelecionarLetras(jogadorNome[contadorIndexLetraAddRank-1 ],1)
                    print(jogadorNome)


            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and contadorIndexMenuAddRank != 1:

                    # Salvar
                    if contadorIndexMenuAddRank == 2:
                        pontuador.salvarPontuação([''.join(jogadorNome),pontuacao])
                        MenuAddRank = False
                        jogadorNome = ["A", "A", "A"]
                        diferençatempo = tempo
                        MenuPrincipal = True

                    # Créditos
                    if contadorIndexMenuAddRank == 3:
                        jogadorNome = ["A", "A", "A"]
                        MenuAddRank = False
                        diferençatempo = tempo
                        MenuPrincipal = True

        if MenuRank:
            pontuador.lerPontuação()
            UI.menuRank(screen,pontuador.matrizPontuação)

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and diferençatempo != tempo:
                    diferençatempo = tempo
                    MenuRank = False
                    MenuPrincipal = True



        if event.type == pg.QUIT:  # If user clicked close
            JogoAtivo = False  # Flag that we are done so we exit this loop
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_h:
                oi.reiniciarMapa()
                Desenhar()
                foi = True
            if event.key == pg.K_m:
                UI.menuPrincipal(screen,0)
            if event.key == pg.K_n:
                EmJogo = False
                foi = False
                MenuAddRank = True
            if event.key == pg.K_p:
                pontuacao += 40


    # Set the screen background
    if foi == True:
        for i in range(len(oi.mapa)-10):
            for j in range(len(oi.mapa[0])-10):
                screen.blit(oi.mapa[i][j].texturaDoTile, (j * TamanhoTile, i * TamanhoTile))
                # =================================
                elementos.coelho.dashEvento(event)
                elementos.coelho.puloCarregado(event)
    
    elementos.coelho.vida()
    elementos.coelho.movimentoBasico()
    elementos.cenoura.movimentoBasico()

    elementos.hit()

    elementos.spritesGerais.draw(screen)
    # ===================================

    screen.blit(pg.image.load('texturas/tiles/ruina/Ruina.png').convert(),(200,0+(int(tempo*0.1))))

    tempo += clock.get_time()

    if tempo >= 10000:
        tempo = 0



    if EmJogo:
        tempoEmJogo = int((pg.time.get_ticks() - tempoInicial) / 1000)
        if tempoEmJogo != tempoDiferencial:
            tempoDiferencial = tempoEmJogo
            pontuacao-=1

        if pontuacao > 9999:
            pontuacao = 9999
        elif pontuacao < 0:
            pontuacao = 0

        painelPontuação = pontuacao

        if painelPontuação >= 1000:
            pass
        elif painelPontuação >= 100:
            painelPontuação = ("0" + str(painelPontuação))
        elif painelPontuação >= 10:
            painelPontuação = ("00" + str(painelPontuação))
        elif painelPontuação >= 0:
            painelPontuação = ("000" + str(painelPontuação))

        screen.blit(font.render("%s" % str(painelPontuação), True, (117, 43, 0)), (200, 0))



    diferençatempo = -1

    pg.display.set_caption(str(int(clock.get_fps())))
    clock.tick(30)
    pg.display.flip()
