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
from os import path
import sys
import random

from src.Elementos_Personagens.Elementos import Personagens

pg.init()

diretorioImg = path.join(path.dirname(__file__), 'SpritesRefatorados')

spriteInit = pg.image.load(path.join(diretorioImg, "SkyBunny_Back.png"))

tamanhoTela = {'x': 1280,
               'y': 720
}

screen = pg.display.set_mode((tamanhoTela['x'],tamanhoTela['y']))

# =======================================

x = tamanhoTela['x']/2
y = tamanhoTela['y']/2
hit = False

elementos: Personagens = Elementos.Personagens(x, y, diretorioImg)


grade = MG.MapGenerator(80,110,screen, elementos,1)
grade.inicializarIlhas()
grade.popularMapa()
grade.texturizarMapa()

pontuador = PN.Pontuador()
pontuador.lerPontuação()

TamanhoTile = grade.texturizador.tamanhoTexturas

UI = MN.Menus()

pg.display.set_caption("Sky Bunny: In Nimbus Island")

def Desenhar():
    grade.texturizarMapa()

font = pg.font.Font("fontes/Retro Gaming.ttf", 16*4)
clock = pg.time.Clock()

tempo = 0
tempoInicial = 0
tempoDiferencial = 0
tempoTransicao = 0

tempoPulo = 0
tempoDePulo = 0

JogoAtivo = True
transicao = False

#MENUS

indexTelas = {
    "Principal": True,
    "Opções": False,
    "Créditos": False,
    "Ranking": False,
    "AdicionarRanking": False,
    "Jogo": False,
    "Transicao": False
}

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
#pg.mixer.music.load('musica/Música2.wav')
pg.mixer.music.play(loops=-1, start=0.0)
pg.mixer.music.set_volume(volume)

# ==================================================

CameraX = tamanhoTela['x']/2
CameraY = tamanhoTela['y']/2

# ==================================================

bg = pg.Surface((tamanhoTela['x'], tamanhoTela['y']))
bg.fill((255, 218, 255))

tilesDaTela = pg.sprite.Group()

fases = 0

def Movimento():
    elementos.coelho.movimentoBasico()
    for cenourasVoadoras in elementos.cenouras:
        if cenourasVoadoras.qualIlha == elementos.coelho.qualIlha:
            cenourasVoadoras.movimentoBasico()
    for charger in elementos.chargers:
        if charger.qualIlha == elementos.coelho.qualIlha:
            charger.movimentoBasico()
    for tiro in elementos.tirosSprite:
        if tiro.qualIlha == elementos.coelho.qualIlha:
            tiro.movimentoBasico()
    for cenourideo in elementos.cenourideos:
        if cenourideo.qualIlha == elementos.coelho.qualIlha:
            cenourideo.movimentoBasico()

def DeteccaoDeDano():
    elementos.coelho.vida()
    elementos.hit()


def trocarMenu(telaOn):

    global indexTelas

    for tela in indexTelas:
        indexTelas[tela] = False

    indexTelas[telaOn] = True

vidaAtual = elementos.coelho.vidas

def reiniciarPartida():

    global pontuacao
    global tempoInicial
    global fases
    global contadorIndexMenu
    global contadorIndexMenuOpções
    global contadorIndexMenuAddRank
    global contadorIndexLetraAddRank
    global jogadorNome

    contadorIndexMenu = 1
    contadorIndexMenuOpções = 1

    contadorIndexMenuAddRank = 1
    contadorIndexLetraAddRank = 1


    elementos.chargers.empty()
    elementos.cenourideos.empty()
    elementos.tirosSprite.empty()
    elementos.cenouras.empty()
    elementos.inimigosSprite.empty()
    for grupo in grade.gruposDeSprite:
        grade.gruposDeSprite[grupo].empty()
    grade.grupoTiles.empty()
    elementos.cenourinhas.empty()
    elementos.coletaveis.empty()

    #elementos.coelho.__init__(tamanhoTela['x'],tamanhoTela['y'], spriteInit)

    fases = 0
    pontuacao = 1000
    jogadorNome = ["A", "A", "A"]
    tempoInicial = pg.time.get_ticks()


    grade.reiniciarMapa(fases)
    Desenhar()

    for sprite in grade.grupoTiles:
        sprite.image.convert()
    for portal in grade.gruposDeSprite["PortalDesativado"]:
        elementos.coelho.rect.x = portal.rect.x + 24
        elementos.coelho.rect.y = portal.rect.y - 24

    elementos.coelho.hp = 3
    elementos.coelho.morreu = False

    elementos.coelho.dashTimer()
    for sprites in elementos.chargers:
        sprites.investidaTimer()
    for sprites in elementos.cenouras:
        sprites.ativacaoTimer()
    for sprites in elementos.tirosSprite:
        sprites.tiroTimer()

    vidaAtual = elementos.coelho.vidas

    trocarMenu("Jogo")

def reiniciarFase():
    global fases
    global pontuacao

    if fases < 3:
        elementos.chargers.empty()
        elementos.cenourideos.empty()
        elementos.tirosSprite.empty()
        elementos.cenouras.empty()
        elementos.inimigosSprite.empty()
        grade.grupoTiles.empty()
        elementos.cenourinhas.empty()
        elementos.coletaveis.empty()

        grade.reiniciarMapa(fases)
        Desenhar()

        trocarMenu("Jogo")

        elementos.coelho.stun = False
        elementos.coelho.stunTimer = 0
        elementos.coelho.pulo = 0
        elementos.coelho.puloDelay = 0
        elementos.coelho.morreu = False

        for portal in grade.gruposDeSprite["PortalDesativado"]:
            elementos.coelho.rect.x = portal.rect.x + 24
            elementos.coelho.rect.y = portal.rect.y - 24

        elementos.coelho.dashTimer()
        for sprites in elementos.chargers:
            sprites.investidaTimer()
        for sprites in elementos.cenouras:
            sprites.ativacaoTimer()
        for sprites in elementos.tirosSprite:
            sprites.tiroTimer()

        elementos.coelho.hp = 3

    else:
        pontuacao += 1000
        fases = 0
        trocarMenu("AdicionarRanking")


def Morte():
    if elementos.coelho.vidas > 0:
        telaTransicao(0, "Fase")
    else:
        elementos.coelho.vidas = 3
        trocarMenu("AdicionarRanking")

qualComando = ""

def telaTransicao(iniciado,reiniciado):
    global transicao
    global tempoTransicao
    global qualComando
    global fases

    if iniciado == 0 and fases < 3:
        trocarMenu("Transicao")
        qualComando = reiniciado
        transicao = True
        tempoTransicao = pg.time.get_ticks()
    else:
        transicao = False
        if qualComando == "Fase":
            reiniciarFase()
        if qualComando == "Partida":
            reiniciarPartida()

while JogoAtivo:
    event: object
    for event in pg.event.get():  # User did something

        if indexTelas["Jogo"] == False:

            if indexTelas["Principal"] == True:
                # Desenha o menu
                UI.menuPrincipal(screen, contadorIndexMenu)

                if event.type == pg.KEYDOWN:
                    # Baixo direita
                    if event.key == pg.K_DOWN or event.key == pg.K_RIGHT:
                        contadorIndexMenu += 1
                        if contadorIndexMenu > 4:
                            contadorIndexMenu = 1
                    # Cima esquerda
                    if event.key == pg.K_UP or event.key == pg.K_LEFT:
                        contadorIndexMenu -= 1
                        if contadorIndexMenu < 1:
                            contadorIndexMenu = 4

                    # Escolha de menu
                    if event.key == pg.K_SPACE:

                        #Inicia o jogo
                        if contadorIndexMenu == 1:
                            telaTransicao(0,"Partida")

                        # Options
                        if contadorIndexMenu == 2:
                            diferençatempo = tempo
                            trocarMenu("Opções")

                        # Rank
                        if contadorIndexMenu == 3:
                            diferençatempo = tempo
                            trocarMenu("Ranking")

                        #Sai do jogo
                        if contadorIndexMenu == 4:
                            JogoAtivo = False

            if  indexTelas["Opções"] == True:
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

                        #Volta
                        if contadorIndexMenuOpções == 1:
                            trocarMenu("Principal")

                        # Créditos
                        if contadorIndexMenuOpções == 3:
                            diferençatempo = tempo
                            trocarMenu("Créditos")

            if indexTelas["Créditos"] == True:
                UI.menuCréditos(screen)

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE and diferençatempo != tempo:
                        trocarMenu("Opções")

            if indexTelas["AdicionarRanking"] == True:
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

                        jogadorNome = ["A", "A", "A"]
                        diferençatempo = tempo
                        trocarMenu("Principal")

            if indexTelas["Ranking"] == True:
                pontuador.lerPontuação()
                UI.menuRank(screen,pontuador.matrizPontuação)

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE and diferençatempo != tempo:
                        diferençatempo = tempo
                        trocarMenu("Principal")



        if event.type == pg.QUIT:  # If user clicked close
            JogoAtivo = False  # Flag that we are done so we exit this loop

        '''
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_h:
                grade.reiniciarMapa()
                Desenhar()
                trocarMenu("Jogo")
            if event.key == pg.K_m:
                UI.menuPrincipal(screen,0)
            if event.key == pg.K_n:
                trocarMenu("AdicionarRanking")
            if event.key == pg.K_p:
                pontuacao += 40
        '''

        if indexTelas["Jogo"] == True:
            elementos.coelho.dashEvento(event)
            elementos.coelho.puloCarregado(event)
            for sprites in elementos.chargers:
                if sprites.qualIlha == elementos.coelho.qualIlha:
                    sprites.investidaEvento(event)
            for sprites in elementos.cenouras:
                if sprites.qualIlha == elementos.coelho.qualIlha:
                    sprites.ativacaoEvento(event)
            for sprites in elementos.tirosSprite:
                sprites.tiroDistanciaEvento(event)

    # Set the screen background
    if indexTelas["Jogo"] == True:
        screen.blit(bg,(0,0))

        CameraX = elementos.coelho.rect.x-tamanhoTela['x']/2
        CameraY = elementos.coelho.rect.y-tamanhoTela['y']/2

        try:
            for i in range(int((CameraY)/64),int((CameraY+784)/64)):
                for j in range(int((CameraX) / 64), int((CameraX + 1344) / 64)):
                    if grade.mapa[i][j].tipoTerrenoTile != "Céu":
                        screen.blit(grade.mapa[i][j].texturaDoTile, (j * TamanhoTile - int(CameraX), i * TamanhoTile - int(CameraY)))
                        tilesDaTela.add(grade.mapa[i][j])
        except:
            pass

    # =================================
        if elementos.coelho.prepPulo == True:
            tempoPulo = int((pg.time.get_ticks() - tempoDePulo) / 1000)
        else:
            tempoDePulo = pg.time.get_ticks()
            tempoPulo = 0



        Movimento()
        DeteccaoDeDano()

        #elementos.spritesGerais.draw(screen)
        for sprites in elementos.inimigosSprite:
            screen.blit(sprites.image,(sprites.rect.x-int(CameraX),sprites.rect.y-int(CameraY)))


        for coletavel in elementos.cenourinhas:
            screen.blit(coletavel.image, (coletavel.rect.x - int(CameraX), coletavel.rect.y - int(CameraY)))

        for tiro in elementos.tirosSprite:
            screen.blit(tiro.image, (tiro.rect.x - int(CameraX), tiro.rect.y - int(CameraY)))

        elementos.hitbox.rect.x = elementos.coelho.rect.x
        elementos.hitbox.rect.y = elementos.coelho.rect.y + 40

        screen.blit(elementos.coelho.image,(elementos.coelho.rect.x-int(CameraX),elementos.coelho.rect.y-int(CameraY)))
        #screen.blit(elementos.hitbox.image,(elementos.coelho.rect.x-int(CameraX),elementos.coelho.rect.y-int(CameraY)+40))

        hit = False #                                grade.grupoTiles
        hit = pg.sprite.spritecollide(elementos.coelho.hitbox,tilesDaTela, False) #elementos.coelho
        if not hit:
            elementos.coelho.vidas -= 1

        try:
            elementos.coelho.qualIlha = hit[0].idIlha
        except:
            elementos.coelho.qualIlha = -1


        coletou = pg.sprite.spritecollide(elementos.coelho, elementos.cenourinhas,True)
        if coletou:
            pontuacao += 100


        teleportando = False
        teleportando = pg.sprite.spritecollide(elementos.coelho, grade.gruposDeSprite["PortalAtivo"], False)
        if teleportando:
            fases += 1
            pontuacao += 500
            telaTransicao(0, "Fase")





    # ===================================

        tempoEmJogo = int((pg.time.get_ticks() - tempoInicial) / 1000)

        if tempoEmJogo != tempoDiferencial:
            tempoDiferencial = tempoEmJogo
            pontuacao-=1
            if pontuacao > 9999:
                pontuacao = 9999
            elif pontuacao < 0:
                pontuacao = 0

        UI.gameHUD(screen,pontuacao,elementos.coelho,tempoPulo)

        if vidaAtual != elementos.coelho.vidas:
            vidaAtual = elementos.coelho.vidas
            Morte()



    #print("HP: %s  ///  Vidas: %s" % (elementos.coelho.hp,elementos.coelho.vidas))

    # = = = = = TRANSIÇÃO AONDE APARECE AS VIDAS DO JOGADOR = = = = = #

    if transicao == True:
        tempoTransicaoPassado = int((pg.time.get_ticks() - tempoTransicao) / 1000)

        UI.gameTransicao(screen, elementos.coelho)

        if tempoTransicaoPassado == 2:
            telaTransicao(1,"-")

    # = = = = = TEMPO = = = = = #


    tilesDaTela.empty()

    tempo += clock.get_time()

    if tempo >= 10000:
        tempo = 0

    diferençatempo = -1

    pg.display.set_caption("Sky Bunny: In Nimbus Island | FPS: %s" % (str(int(clock.get_fps()))))
    clock.tick(30)
    pg.display.flip()








