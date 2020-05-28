import src.TileInfo as TileInfo
import random
import pygame as pg

class TexturaUI:
    def __init__(self, idTextura, tipoTextura, caminhoTextura):

        self.idTextura = idTextura
        self.tipoTextura = tipoTextura
        self.caminhoTextura = caminhoTextura

class Menus:

    tamanhoTexturasX = 60
    tamanhoTexturasY = 12
    listaDeTexturas = []

    def __init__(self):
        self.listaDeTexturas = [
            TexturaUI(0, "Background", pg.transform.scale(pg.image.load("texturas/interfaces/Fundo_Menu.png"), (304*4, 208*4))),

            TexturaUI(1, "MenuInicial", [self.carregarImagem("texturas/interfaces/StartOff.png"),self.carregarImagem("texturas/interfaces/StartOn.png")]),
            TexturaUI(2, "MenuInicial", [self.carregarImagem("texturas/interfaces/LoadOff.png"),self.carregarImagem("texturas/interfaces/LoadOn.png")]),
            TexturaUI(3, "MenuInicial", [self.carregarImagem("texturas/interfaces/Options.png"),self.carregarImagem("texturas/interfaces/OptionsOn.png")]),
            TexturaUI(4, "MenuInicial", [self.carregarImagem("texturas/interfaces/Rank.png"), self.carregarImagem("texturas/interfaces/RankOn.png")]),
            TexturaUI(5, "MenuInicial", [self.carregarImagem("texturas/interfaces/Quit.png"), self.carregarImagem("texturas/interfaces/QuitOn.png")]),

            #TexturaUI(1, "MenuFase", [self.carregarImagem(""), self.carregarImagem("")]),
            #TexturaUI(2, "MenuFase", [self.carregarImagem(""), self.carregarImagem("")]),

            TexturaUI(1, "MenuOpções", [pg.transform.scale(pg.image.load("texturas/interfaces/BackOff.png"), (13*4, 14*4)), pg.transform.scale(pg.image.load("texturas/interfaces/BackOn.png"), (13*4, 14*4))]),
            TexturaUI(2, "MenuOpções", [pg.transform.scale(pg.image.load("texturas/interfaces/SoundOff.png"), (82*4, 16*4)), pg.transform.scale(pg.image.load("texturas/interfaces/SoundOn.png"), (82*4, 16*4))]),
            TexturaUI(3, "MenuOpções", [self.carregarImagem("texturas/interfaces/CreditosOff.png"), self.carregarImagem("texturas/interfaces/CreditosOn.png")]),
            TexturaUI(4, "MenuOpções", [pg.transform.scale(pg.image.load("texturas/interfaces/SliderOff.png"), (5*4, 14*4)), pg.transform.scale(pg.image.load("texturas/interfaces/SliderOn.png"), (5*4, 14*4))]),

            TexturaUI(1, "MenuCréditos", [pg.transform.scale(pg.image.load("texturas/interfaces/BackOn.png"), (13*4, 14*4))]),
            TexturaUI(2, "MenuCréditos", [pg.transform.scale(pg.image.load("texturas/interfaces/TelaCreditos.png"), (175*4, 95*4))]),

            TexturaUI(1, "MenuAddRank", [pg.transform.scale(pg.image.load("texturas/interfaces/SayYourName.png"), (130 * 4, 12 * 4))]),
            TexturaUI(2, "MenuAddRank", [pg.transform.scale(pg.image.load("texturas/interfaces/RankTable.png"), (60 * 4, 19 * 4))]),
            TexturaUI(3, "MenuAddRank", [pg.transform.scale(pg.image.load("texturas/interfaces/CharSelectorON.png"), (14 * 4, 52 * 4)),pg.transform.scale(pg.image.load("texturas/interfaces/CharSelectorOFF.png"), (14 * 4, 52 * 4))]),
            TexturaUI(4, "MenuAddRank", [self.carregarImagem("texturas/interfaces/SaveOff.png"),self.carregarImagem("texturas/interfaces/SaveOn.png")]),
            TexturaUI(5, "MenuAddRank", [self.carregarImagem("texturas/interfaces/SkipOff.png"),self.carregarImagem("texturas/interfaces/LoadOn.png")]),
        ]


    def carregarImagem(self,caminho):
        return pg.transform.scale(pg.image.load(caminho), (self.tamanhoTexturasX*4, self.tamanhoTexturasY*4))


    def menuPrincipal(self, tela, index):
        tela.blit(self.listaDeTexturas[0].caminhoTextura, (-10,-50))

        ordenador = 1

        for UI in self.listaDeTexturas:
            if UI.tipoTextura == "MenuInicial":
                if index == UI.idTextura:
                    tela.blit(UI.caminhoTextura[1], (250, 120 + (75 * ordenador)))
                else:
                    tela.blit(UI.caminhoTextura[0], (250, 120 + (75 * ordenador)))
                ordenador += 1

    def menuOpções(self, tela, index, volume):
        tela.blit(self.listaDeTexturas[0].caminhoTextura, (-10,-50))

        ordenador = 1

        for UI in self.listaDeTexturas:
            if UI.tipoTextura == "MenuOpções":
                if index == UI.idTextura:
                    tela.blit(UI.caminhoTextura[1], (250,(140 * ordenador)))
                else:
                    if UI.idTextura == 4 and index == 2:
                        tela.blit(UI.caminhoTextura[1], (386+int(115*volume), 283))
                    elif UI.idTextura == 4 and index != 2:
                        tela.blit(UI.caminhoTextura[0], (386+int(115*volume), 283))
                    else:
                        tela.blit(UI.caminhoTextura[0], (250, (140 * ordenador)))
                ordenador += 1

    def menuCréditos(self, tela):
        tela.blit(self.listaDeTexturas[0].caminhoTextura, (-10,-50))

        for UI in self.listaDeTexturas:
            if UI.tipoTextura == "MenuCréditos":
                if UI.idTextura == 1:
                    tela.blit(UI.caminhoTextura[0], (250, 140))
                if UI.idTextura == 2:
                    tela.blit(UI.caminhoTextura[0], (250,210))


    def menuAddRank(self, tela):
        tela.blit(self.listaDeTexturas[0].caminhoTextura, (-10,-50))

        for UI in self.listaDeTexturas:
            if UI.tipoTextura == "MenuAddRank":
                if UI.idTextura == 1: #603
                    tela.blit(UI.caminhoTextura[0], (343, 135))
                if UI.idTextura == 2:
                    tela.blit(UI.caminhoTextura[0], (483,190))
                if UI.idTextura == 3:
                    tela.blit(UI.caminhoTextura[0], (460, 300))
                    tela.blit(UI.caminhoTextura[0], (575, 300))
                    tela.blit(UI.caminhoTextura[0], (690, 300))
                if UI.idTextura == 4:
                    tela.blit(UI.caminhoTextura[0], (343,550))
                if UI.idTextura == 5:
                    tela.blit(UI.caminhoTextura[0], (623,550))




