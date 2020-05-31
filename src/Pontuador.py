import src.TileInfo as TileInfo
import random
import pygame as pg

class Pontuador:
    def __init__(self):

        self.matrizPontuação = []

    def salvarPontuação(self,registro):

        if registro[1] >= 1000:
            pass
        elif registro[1] >= 100:
            registro[1] = ("0" + str(registro[1]))
        elif registro[1] >= 10:
            registro[1] = ("00" + str(registro[1]))
        elif registro[1] >= 0:
            registro[1] = ("000" + str(registro[1]))

        if int(registro[1]) >= int(self.matrizPontuação[len(self.matrizPontuação)-1][1]):
            self.matrizPontuação[len(self.matrizPontuação)-1] = registro

        for j in range(len(self.matrizPontuação) - 1, 0, -1):
            for i in range(j):
                if int(self.matrizPontuação[i][1]) < int(self.matrizPontuação[i + 1][1]):
                    temp = self.matrizPontuação[i]
                    self.matrizPontuação[i] = self.matrizPontuação[i + 1]
                    self.matrizPontuação[i + 1] = temp

        print(self.matrizPontuação)

        with open("saves/rank.txt","w") as arquivoTxt:
            for rank in self.matrizPontuação:
                arquivoTxt.write("%s %s\n" % (rank[0], rank[1]))

    def lerPontuação(self):
        with open("saves/rank.txt") as arquivoTxt:
            self.matrizPontuação = [linha.split() for linha in arquivoTxt]