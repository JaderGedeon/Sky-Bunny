import os
import random
import pygame

import src.TileInfo as TileInfo

# Cada unidade de medida se refere a um Tile

# Dicionário de texturas
#
#     0 = Céu
#     1 = Terra
#

class IslandsInfo:
    def __init__(self, matrixIlha, comprimentoIlha, alturaIlha):
        self.matrixIlha = matrixIlha
        self.comprimentoIlha = comprimentoIlha
        self.alturaIlha = alturaIlha

class MapGenerator:
    mapa = []
    listaDeIlhas = []

    dimensoesIlha = {
        "maiorComprimento": 0,
        "maiorAltura": 0,
    }

    def __init__(self, comprimento, altura):
        self.comprimento = comprimento
        self.altura = altura

        # Cria um mapa com tamanho X e Y baseados nos valores de inicialização
        self.mapa = [[TileInfo.Tile(0,0) for x in range(comprimento)] for y in range(altura)]


    def inicializarIlhas(self):
        # Lê todos os arquivos de Presets/Islands/
        arquivosDeIlhas = os.listdir("Presets/Islands/")
        # Filtra os arquivos .txt
        arquivosDeIlhas = [arquivo for arquivo in arquivosDeIlhas if arquivo.endswith(".txt")]

        for ilhaTexto in arquivosDeIlhas:
            # Lê o arquivo .txt da ilha
            with open("Presets/Islands/%s" % ilhaTexto) as arquivoTxt:
                matrixIlha = [linha.split() for linha in arquivoTxt]

            # Descobre as maiores e menores dimensões das ilhas e armazena os valores em dimensoesIlha

            if len(matrixIlha[0]) > self.dimensoesIlha["maiorComprimento"]:
                self.dimensoesIlha["maiorComprimento"] = len(matrixIlha[0])

            if len(matrixIlha) > self.dimensoesIlha["maiorAltura"]:
                self.dimensoesIlha["maiorAltura"] = len(matrixIlha)


            # Inicializa e da append num novo objeto de ilha baseada nas informações do txt (Matrix,TamanhoX,TamanhoY)
            self.listaDeIlhas.append(IslandsInfo(matrixIlha,len(matrixIlha[0]),len(matrixIlha)))

    def popularMapa(self):

        identificadorDeIlhas = 0

        # Da o full scan no mapa para começar a populá-lo
        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[0])):

                if self.mapa[i][j].texturaDoTile == 0:

                    espacoLivre = {
                        "comprimento": 0,
                        "altura": 0
                    }

                    # Verifica se não vai dar ArrayOutOfRange
                    # Se o espaço livre não é maior do que a maior ilha
                    # E se o espaço subsequente está em branco

                    while j + espacoLivre["comprimento"] < len(self.mapa[0]) and\
                            espacoLivre["comprimento"] < self.dimensoesIlha["maiorComprimento"] and\
                            self.mapa[i][j + espacoLivre["comprimento"]].texturaDoTile == 0:

                        espacoLivre["comprimento"] += 1

                    while i + espacoLivre["altura"] < len(self.mapa) and\
                            espacoLivre["altura"] < self.dimensoesIlha["maiorAltura"] and\
                            self.mapa[i + espacoLivre["altura"]][j].texturaDoTile == 0:

                        espacoLivre["altura"] += 1


                    random.shuffle(self.listaDeIlhas)

                    # Procura a primeira ilha no array de ilhas que encaixe no espaço livre
                    for ilha in self.listaDeIlhas:
                        if ilha.comprimentoIlha <= espacoLivre["comprimento"] and ilha.alturaIlha <= espacoLivre["altura"]:
                            identificadorDeIlhas += 1
                            for iIlha in range(ilha.alturaIlha):
                                for jIlha in range(ilha.comprimentoIlha):
                                    if ilha.matrixIlha[iIlha][jIlha] != 0:
                                        self.mapa[i+iIlha][j+jIlha].idIlha = identificadorDeIlhas
                                        self.mapa[i + iIlha][j + jIlha].texturaDoTile = ilha.matrixIlha[iIlha][jIlha]
                            break

    def texturizarMapa(self):

        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[0])):
                pass

    def reiniciarMapa(self):
        self.mapa = [[TileInfo.Tile(0,0) for x in range(self.comprimento)] for y in range(self.altura)]
        MapGenerator.popularMapa(self)
