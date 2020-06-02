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

from src.Elementos_Personagens.Elementos import Personagens

pg.init()

WINDOW_SIZE = [1280, 720]
screen = pg.display.set_mode(WINDOW_SIZE)

grade = MG.MapGenerator(80,110,screen)
grade.inicializarIlhas()
grade.popularMapa()
grade.texturizarMapa()

pontuador = PN.Pontuador()
pontuador.lerPontuação()

TamanhoTile = grade.texturizador.tamanhoTexturas

UI = MN.Menus()

pg.display.set_caption("RODA MEU DEUS")

JogoAtivo = True

def Desenhar():
    grade.texturizarMapa()

font = pg.font.Font("fontes/Retro Gaming.ttf", 16*4)
clock = pg.time.Clock()

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
pg.mixer.music.load('musica/skyloop.wav')
pg.mixer.music.play(loops=-1, start=0.0)
pg.mixer.music.set_volume(volume)

# ==================================================

x = 1280/2
y = 720/2
hit = False

elementos: Personagens = Elementos.Personagens(x, y)

# Timers
elementos.coelho.dashTimer()
for sprites in elementos.chargers:
    sprites.investidaTimer()
for sprites in elementos.cenouras:
    sprites.ativacaoTimer()
for sprites in elementos.tirosSprite:
    sprites.tiroTimer()


CameraX = 1280/2
CameraY = 720/2

# ==================================================


def ReiniciarJogo():
    screen.fill((0, 0, 0))
    global pontuacao
    pontuacao = 1000
    grade.reiniciarMapa()
    Desenhar()

    global tempoInicial
    tempoInicial = pg.time.get_ticks()
    global EmJogo
    EmJogo = True
    global fases
    fases = 0

bg = pg.Surface((1280, 720))
bg.fill((255, 218, 255))

tilesDaTela = pg.sprite.Group()

fases = 0

def Movimento():
    elementos.coelho.movimentoBasico()
    for sprites in elementos.cenouras:
        sprites.movimentoBasico()
    for sprites in elementos.chargers:
       sprites.movimentoBasico()
    for sprites in elementos.tirosSprite:
        sprites.movimentoBasico()
    for sprites in elementos.cenourideos:
        sprites.movimentoBasico()

def DeteccaoDeDano():
    elementos.coelho.vida()
    elementos.hit()

while JogoAtivo:
    event: object
    for event in pg.event.get():  # User did something

        if EmJogo != True:

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
                            ReiniciarJogo()
                            for sprite in grade.grupoTiles:
                                sprite.image.convert()
                            for portal in grade.gruposDeSprite["PortalDesativado"]:
                                elementos.coelho.rect.x = portal.rect.x+24
                                elementos.coelho.rect.y = portal.rect.y-24

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
                grade.reiniciarMapa()
                Desenhar()
                EmJogo = True
            if event.key == pg.K_m:
                UI.menuPrincipal(screen,0)
            if event.key == pg.K_n:
                EmJogo = False
                MenuAddRank = True
            if event.key == pg.K_p:
                pontuacao += 40

        if EmJogo == True:
            elementos.coelho.dashEvento(event)
            elementos.coelho.puloCarregado(event)
            for sprites in elementos.chargers:
                sprites.investidaEvento(event)
            for sprites in elementos.cenouras:
                sprites.ativacaoEvento(event)
            for sprites in elementos.tirosSprite:
                sprites.tiroDistanciaEvento(event)

    # Set the screen background
    if EmJogo == True:
        screen.blit(bg,(0,0))

        CameraX = elementos.coelho.rect.x-1280/2
        CameraY = elementos.coelho.rect.y-720/2

        try:
            for i in range(int((CameraY)/64),int((CameraY+784)/64)):
                for j in range(int((CameraX) / 64), int((CameraX + 1344) / 64)):
                    if grade.mapa[i][j].tipoTerrenoTile != "Céu":
                        screen.blit(grade.mapa[i][j].texturaDoTile, (j * TamanhoTile - int(CameraX), i * TamanhoTile - int(CameraY)))
                        tilesDaTela.add(grade.mapa[i][j])
        except:
            pass

        '''
        for sprites in grade.grupoTiles:
            if sprites.rect.x - int(CameraX) <= 1400 and sprites.rect.x - int(CameraX) >= -100 and\
                    sprites.rect.y - int(CameraY) <= 850 and sprites.rect.y - int(CameraY) >= -100:
                screen.blit(sprites.image,(sprites.rect.x-int(CameraX),sprites.rect.y-int(CameraY)))
        '''


        for inimigo in grade.inimigos:
            imagem = inimigo[0]
            imagem.fill(inimigo[2])
            retangulo = imagem.get_rect()
            screen.blit(imagem, (inimigo[1][0]-int(CameraX),inimigo[1][1]-int(CameraY)))


    # =================================

        Movimento()
        DeteccaoDeDano()

        #elementos.spritesGerais.draw(screen)
        for sprites in elementos.spritesGerais:
            screen.blit(sprites.image,(sprites.rect.x-int(CameraX),sprites.rect.y-int(CameraY)))

        pulando = False
        if not pulando:
            hit = False #                                grade.grupoTiles
            hit = pg.sprite.spritecollide(elementos.coelho,tilesDaTela, False)
            if not hit:
                print("No céu")

        teleportando = False
        teleportando = pg.sprite.spritecollide(elementos.coelho, grade.gruposDeSprite["PortalAtivo"], False)
        if teleportando:
            fases += 1
            screen.fill((255,255,255))
            if fases < 3:
                grade.reiniciarMapa()
                Desenhar()
                for portal in grade.gruposDeSprite["PortalDesativado"]:
                    elementos.coelho.rect.x = portal.rect.x + 24
                    elementos.coelho.rect.y = portal.rect.y - 24
            else:
                EmJogo = False
                MenuAddRank = True





    # ===================================

        tempoEmJogo = int((pg.time.get_ticks() - tempoInicial) / 1000)

        if tempoEmJogo != tempoDiferencial:
            tempoDiferencial = tempoEmJogo
            pontuacao-=1
            if pontuacao > 9999:
                pontuacao = 9999
            elif pontuacao < 0:
                pontuacao = 0

        UI.gameHUD(screen,pontuacao)




    ## Continuação Normal

    screen.blit(pg.image.load('texturas/tiles/ruina/Ruina.png').convert(),(200,0+(int(tempo*0.1))))

    tempo += clock.get_time()

    if tempo >= 10000:
        tempo = 0

    diferençatempo = -1

    tilesDaTela.empty()

    pg.display.set_caption(str(int(clock.get_fps())))
    clock.tick(60)
    pg.display.flip()








