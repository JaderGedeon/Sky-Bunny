import os
import random
import pygame

import src.TileInfo as TileInfo
import src.TexturesInfo as TexturesInfo

# Cada unidade de medida se refere a um Tile

class IslandsInfo:
    def __init__(self, matrixIlha, comprimentoIlha, alturaIlha):
        self.matrixIlha = matrixIlha
        self.comprimentoIlha = comprimentoIlha
        self.alturaIlha = alturaIlha

class MapGenerator:
    texturizador = 0

    inimigos = []

    conjuntoIlhas = []

    grupoTiles = pygame.sprite.Group()

    mapa = []
    listaDeIlhas = []
    listaDeIlhasTransitorias = []

    gruposDeSprite = {
        "Chão": pygame.sprite.Group(),
        "Ruína": pygame.sprite.Group(),
        "Parede": pygame.sprite.Group(),
        "PortalAtivo": pygame.sprite.Group(),
        "PortalDesativado": pygame.sprite.Group(),
    }



    dimensoesIlha = {
        "maiorComprimento": 0,
        "maiorAltura": 0,
    }

    areasTransitórias = {
        "altura": 25,
        "comprimento": 15, #Fica em 0, tá aqui para caso precisarmos fazer alguma mudança
    }

    def __init__(self, comprimento, altura,screen):
        self.comprimento = comprimento
        self.altura = altura
        self.screen = screen

        self.texturizador = TexturesInfo.TexturasMapa(screen)

        # Cria um mapa com tamanho X e Y baseados nos valores de inicialização
        self.mapa = [[TileInfo.Tile(None,"","",0,0,0) for x in range(comprimento)] for y in range(altura)]


    def inicializarIlhas(self):
        
        # Dicionário com os tipos de terreno
        dicionarioTipoTerreno = {
            '0': "Céu",
            '1': "Grama",
            '2': "Ruina",

            '8': "Parede",
            '9': "Portal",
        }

        # Lê todos os arquivos de Presets/Islands/
        arquivosDeIlhas = os.listdir("predefinicoes/ilhas/")
        # Filtra os arquivos .txt
        arquivosDeIlhas = [arquivo for arquivo in arquivosDeIlhas if arquivo.endswith(".txt")]

        for ilhaTexto in arquivosDeIlhas:
            # Lê o arquivo .txt da ilha
            with open("predefinicoes/ilhas/%s" % ilhaTexto) as arquivoTxt:
                matrixIlha = [linha.split() for linha in arquivoTxt]

            # Converte os caracteres das ilhas para palavras baseadas no dicionário
            for i in range(len(matrixIlha)):
                for j in range(len(matrixIlha[0])):
                    matrixIlha[i][j] = dicionarioTipoTerreno[matrixIlha[i][j]]

            # Descobre as maiores dimensões das ilhas e armazena os valores em dimensoesIlha
            if len(matrixIlha[0]) > self.dimensoesIlha["maiorComprimento"]:
                self.dimensoesIlha["maiorComprimento"] = len(matrixIlha[0])

            if len(matrixIlha) > self.dimensoesIlha["maiorAltura"]:
                self.dimensoesIlha["maiorAltura"] = len(matrixIlha)


            # Inicializa e da append num novo objeto de ilha baseada nas informações do txt (Matrix,TamanhoX,TamanhoY)
            self.listaDeIlhas.append(IslandsInfo(matrixIlha,len(matrixIlha[0]),len(matrixIlha)))



        # Ilhas Transitórias

        arquivosDeIlhas = os.listdir("predefinicoes/ilhasTransitorias/")
        # Filtra os arquivos .txt
        arquivosDeIlhas = [arquivo for arquivo in arquivosDeIlhas if arquivo.endswith(".txt")]

        for ilhaTexto in arquivosDeIlhas:
            # Lê o arquivo .txt da ilha
            with open("predefinicoes/ilhasTransitorias/%s" % ilhaTexto) as arquivoTxt:
                matrixIlha = [linha.split() for linha in arquivoTxt]

            # Converte os caracteres das ilhas para palavras baseadas no dicionário
            for i in range(len(matrixIlha)):
                for j in range(len(matrixIlha[0])):
                    matrixIlha[i][j] = dicionarioTipoTerreno[matrixIlha[i][j]]

            self.listaDeIlhasTransitorias.append(IslandsInfo(matrixIlha, len(matrixIlha[0]), len(matrixIlha)))

    def popularMapa(self):
        self.inimigos = []
        self.conjuntoIlhas = []
        self.grupoTiles = pygame.sprite.Group()

        for items in self.gruposDeSprite:
            items = pygame.sprite.Group()

        identificadorDeIlhas = 2
        idTotal = 0

        # Da o full scan no mapa para começar a populá-lo
        for i in range(1+self.areasTransitórias["altura"],len(self.mapa)-(1+self.areasTransitórias["altura"])):
            for j in range(1+self.areasTransitórias["comprimento"],len(self.mapa[0])-(1+self.areasTransitórias["comprimento"])):

                if self.mapa[i][j].tipoTerrenoTile == None:


                    espacoLivre = {
                        "comprimento": 0,
                        "altura": 0
                    }


                    # Verifica se não vai dar ArrayOutOfRange
                    # Se o espaço livre não é maior do que a maior ilha
                    # E se o espaço subsequente está em branco

                    while j + espacoLivre["comprimento"] < len(self.mapa[0])-(1+self.areasTransitórias["comprimento"]) and\
                            espacoLivre["comprimento"] < self.dimensoesIlha["maiorComprimento"] and\
                            self.mapa[i][j + espacoLivre["comprimento"]].tipoTerrenoTile == None:

                        espacoLivre["comprimento"] += 1

                    while i + espacoLivre["altura"] < len(self.mapa) - self.areasTransitórias["altura"] and\
                            espacoLivre["altura"] < self.dimensoesIlha["maiorAltura"] and\
                            self.mapa[i + espacoLivre["altura"]][j].tipoTerrenoTile == None:

                        espacoLivre["altura"] += 1


                    random.shuffle(self.listaDeIlhas)

                    # Procura a primeira ilha no array de ilhas que encaixe no espaço livre
                    for ilha in self.listaDeIlhas:
                        if ilha.comprimentoIlha <= espacoLivre["comprimento"] and ilha.alturaIlha <= espacoLivre["altura"]:
                            identificadorDeIlhas += 1
                            # Copia o formato da ilha para o mapa, passando também o ID da ilha para cada terreno
                            for iIlha in range(ilha.alturaIlha):
                                for jIlha in range(ilha.comprimentoIlha):
                                    if ilha.matrixIlha[iIlha][jIlha] != "Céu":
                                        self.mapa[i+iIlha][j+jIlha].idIlha = identificadorDeIlhas
                                    self.mapa[i + iIlha][j + jIlha].tipoTerrenoTile = ilha.matrixIlha[iIlha][jIlha]
                            break

        # Substitui None por Céu // Rever num futuro próximo

        idTotal = identificadorDeIlhas+1
        self.conjuntoIlhas = [[] for y in range(idTotal)]

        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[0])):
                if self.mapa[i][j].tipoTerrenoTile == None:
                    self.mapa[i][j].tipoTerrenoTile = "Céu"



        # Identificando os tiles mais perto do topo

        listaDeTilesSuperiores = []

        for iTiles in range(1 + self.areasTransitórias["altura"], len(self.mapa) - (1 + self.areasTransitórias["altura"])):
            for jTiles in range(1+self.areasTransitórias["comprimento"],len(self.mapa[0])-(1+self.areasTransitórias["comprimento"])):
                if self.mapa[iTiles][jTiles].tipoTerrenoTile != "Céu":
                    listaDeTilesSuperiores.append([iTiles,jTiles])
            if listaDeTilesSuperiores != []:
                break

        # Identificando os tiles mais perto de baixo

        listaDeTilesInferiores = []

        # Localiza o index inferior
        for i in range(len(self.mapa) - (1 + self.areasTransitórias["altura"]),1 + self.areasTransitórias["altura"],-1):
            for j in range(len(self.mapa[0]) - (1 + self.areasTransitórias["comprimento"]),1 + self.areasTransitórias["comprimento"],-1):
                if self.mapa[i][j].tipoTerrenoTile != "Céu":
                    listaDeTilesInferiores.append([i,j])
            if listaDeTilesInferiores != []:
                break


        # Coloca a ilha de transição do topo

        random.shuffle(listaDeTilesSuperiores)

        for ilhaT in self.listaDeIlhasTransitorias:
            identificadorDeIlhas = 2

            # Copia o formato da ilha para o mapa, passando também o ID da ilha para cada terreno
            for iIlhaT in range(ilhaT.alturaIlha-1, 0, -1):
                for jIlhaT in range(ilhaT.comprimentoIlha-1, 0, -1):
                    if ilhaT.matrixIlha[iIlhaT][jIlhaT] != "Céu":
                        self.mapa[listaDeTilesSuperiores[0][0]-1 - iIlhaT][listaDeTilesSuperiores[0][1]+5 - jIlhaT].idIlha = identificadorDeIlhas
                    self.mapa[listaDeTilesSuperiores[0][0]-1 - iIlhaT][listaDeTilesSuperiores[0][1]+5 - jIlhaT].tipoTerrenoTile = ilhaT.matrixIlha[ilhaT.alturaIlha-1-iIlhaT][ilhaT.comprimentoIlha-1-jIlhaT]
            break

        # Coloca a ilha de transição de baixo

        random.shuffle(listaDeTilesInferiores)

        for ilhaT in self.listaDeIlhasTransitorias:
            identificadorDeIlhas = 1

            # Copia o formato da ilha para o mapa, passando também o ID da ilha para cada terreno
            for iIlhaT in range(ilhaT.alturaIlha-1, 0, -1):
                for jIlhaT in range(ilhaT.comprimentoIlha-1, 0, -1):
                    if ilhaT.matrixIlha[iIlhaT][jIlhaT] != "Céu":
                        self.mapa[listaDeTilesInferiores[0][0]+1 + iIlhaT][listaDeTilesInferiores[0][1]-5 + jIlhaT].idIlha = identificadorDeIlhas
                    self.mapa[listaDeTilesInferiores[0][0]+1 + iIlhaT][listaDeTilesInferiores[0][1]-5 + jIlhaT].tipoTerrenoTile = ilhaT.matrixIlha[ilhaT.alturaIlha-1-iIlhaT][ilhaT.comprimentoIlha-1-jIlhaT]
            break



        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[0])):
                #if self.mapa[i][j].tipoTerrenoTile != None and self.mapa[i][j].tipoTerrenoTile != "Céu":
                self.mapa[i][j].xTile = j*self.texturizador.tamanhoTexturas
                self.mapa[i][j].yTile = i * self.texturizador.tamanhoTexturas
                self.conjuntoIlhas[self.mapa[i][j].idIlha].append(self.mapa[i][j])
                if self.mapa[i][j].tipoTerrenoTile == None:
                    self.mapa[i][j].tipoTerrenoTile = "Céu"




        # I da ilha de cima : 1 + self.areasTransitórias["altura"] (acho q -1)
        # I da ilha de baixo :

    def texturizarMapa(self):

        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[0])):
                if  self.mapa[i][j].tipoTerrenoTile != "Céu":
                    self.mapa[i][j].formatoTile = "Centro"

                    #Lógica da Grama
                    if self.mapa[i][j].tipoTerrenoTile == "Grama":

                        #BAIXO
                        if self.mapa[i+1][j].tipoTerrenoTile == "Céu":
                            self.mapa[i][j].formatoTile = "Baixo"

                        #CIMA
                        if self.mapa[i-1][j].tipoTerrenoTile == "Céu":
                            self.mapa[i][j].formatoTile = "Cima"

                        #ESQUERDA
                        if self.mapa[i][j-1].tipoTerrenoTile == "Céu":

                            self.mapa[i][j].formatoTile = "Esquerda"

                            if self.mapa[i-1][j].tipoTerrenoTile == "Céu":
                                self.mapa[i][j].formatoTile = "CantoSE"

                            elif self.mapa[i+1][j].tipoTerrenoTile == "Céu":
                                self.mapa[i][j].formatoTile = "CantoIE"
                        else:
                            if self.mapa[i-1][j].tipoTerrenoTile != "Céu" and self.mapa[i-1][j-1].tipoTerrenoTile == "Céu":
                                self.mapa[i][j].formatoTile = "LigacaoSE"
                            elif self.mapa[i+1][j].tipoTerrenoTile != "Céu" and self.mapa[i+1][j-1].tipoTerrenoTile == "Céu":
                                self.mapa[i][j].formatoTile = "LigacaoIE"


                        #DIREITA
                        if self.mapa[i][j+1].tipoTerrenoTile == "Céu":

                            self.mapa[i][j].formatoTile = "Direita"

                            if self.mapa[i-1][j].tipoTerrenoTile == "Céu":
                                self.mapa[i][j].formatoTile = "CantoSD"

                            if self.mapa[i + 1][j].tipoTerrenoTile == "Céu":
                                self.mapa[i][j].formatoTile = "CantoID"
                        else:
                            if self.mapa[i-1][j].tipoTerrenoTile != "Céu" and self.mapa[i-1][j+1].tipoTerrenoTile == "Céu":
                                self.mapa[i][j].formatoTile = "LigacaoSD"
                            elif self.mapa[i+1][j].tipoTerrenoTile != "Céu" and self.mapa[i+1][j+1].tipoTerrenoTile == "Céu":
                                self.mapa[i][j].formatoTile = "LigacaoID"

                        self.gruposDeSprite["Chão"].add(self.mapa[i][j])
                    #Lógica da Ruina
                    elif self.mapa[i][j].tipoTerrenoTile == "Ruina":

                        # ESQUERDA
                        if self.mapa[i][j - 1].tipoTerrenoTile != self.mapa[i][j].tipoTerrenoTile:
                            if self.mapa[i - 1][j].tipoTerrenoTile != self.mapa[i][j].tipoTerrenoTile:
                                self.mapa[i][j].formatoTile = "CantoSE"

                            if self.mapa[i + 1][j].tipoTerrenoTile != self.mapa[i][j].tipoTerrenoTile:
                                if self.mapa[i][j].formatoTile != "Centro":
                                    self.mapa[i][j].formatoTile = "Centro"
                                else:
                                    self.mapa[i][j].formatoTile = "CantoIE"

                        # DIREITA
                        if self.mapa[i][j + 1].tipoTerrenoTile != self.mapa[i][j].tipoTerrenoTile:
                            if self.mapa[i - 1][j].tipoTerrenoTile != self.mapa[i][j].tipoTerrenoTile:
                                self.mapa[i][j].formatoTile = "CantoSD"

                            if self.mapa[i + 1][j].tipoTerrenoTile != self.mapa[i][j].tipoTerrenoTile:
                                if self.mapa[i][j].formatoTile != "Centro":
                                    self.mapa[i][j].formatoTile = "Centro"
                                else:
                                    self.mapa[i][j].formatoTile = "CantoID"

                        self.gruposDeSprite["Ruína"].add(self.mapa[i][j])
                    #Lógica da Parede e Portal
                    elif self.mapa[i][j].tipoTerrenoTile == "Portal":
                        if self.mapa[i][j].idIlha == 2:
                            self.gruposDeSprite["PortalAtivo"].add(self.mapa[i][j])
                        else:
                            self.gruposDeSprite["PortalDesativado"].add(self.mapa[i][j])

                    elif self.mapa[i][j].tipoTerrenoTile == "Parede":
                        self.gruposDeSprite["Parede"].add(self.mapa[i][j])


                    self.mapa[i][j].texturaDoTile = self.texturizador.TexturizarTile(self.mapa[i][j])
                    self.mapa[i][j].desenho()
                    self.grupoTiles.add(self.mapa[i][j])
        self.povoarInimigos()


    def reiniciarMapa(self):
        self.mapa = [[TileInfo.Tile(None,"","",0,0,0) for x in range(self.comprimento)] for y in range(self.altura)]
        MapGenerator.popularMapa(self)
        for grupo in self.gruposDeSprite:
            self.gruposDeSprite[grupo].empty()


    def povoarInimigos(self):

        for conjIlhas in self.conjuntoIlhas:
            if conjIlhas[0].idIlha > 2:
                pesoIlha = 15 #random.randint(15, 20)
                #random.shuffle(coordenadasIlhas)

                while pesoIlha != 0:
                    inimigoSelecionador = random.randint(1, 3)
                    random.shuffle(conjIlhas)
                    if conjIlhas[0].formatoTile == "Centro":
                        if pesoIlha >= 5 and inimigoSelecionador == 1:
                            pesoIlha -= 5
                            self.inimigos.append([pygame.Surface((32, 32)),(conjIlhas[0].xTile,conjIlhas[0].yTile),(25,150,255)])
                        elif pesoIlha >= 3 and inimigoSelecionador == 2:
                            pesoIlha -=3
                            self.inimigos.append([pygame.Surface((32, 32)),(conjIlhas[0].xTile,conjIlhas[0].yTile),(255,137,0)])
                        elif pesoIlha >= 1:
                            pesoIlha -=1
                            self.inimigos.append([pygame.Surface((32, 32)),(conjIlhas[0].xTile,conjIlhas[0].yTile),(125,30,0)])


