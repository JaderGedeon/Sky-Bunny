import os
import src.IslandInfo as IslInf
import random


class MapGenerator:
    mapa = []
    listaDeIlhas = []

    def __init__(self, tamanhoYmapa, tamanhoXmapa):
        self.tamanhoXmapa = tamanhoXmapa
        self.tamanhoYmapa = tamanhoYmapa

        # Cria um mapa com tamanho X e Y baseados nos valores de inicialização
        self.mapa = [['_' for x in range(tamanhoXmapa)] for y in range(tamanhoYmapa)]

    def inicializarIlhas(self):
        #Lê todos os arquivos de Presets/Islands/
        arquivosDeIlhas = os.listdir("Presets/Islands/")
        #Filtra os arquivos .txt
        arquivosDeIlhas = [arquivo for arquivo in arquivosDeIlhas if arquivo.endswith(".txt")]

        for ilha in arquivosDeIlhas:
            #Lê o arquivo txt da ilha
            with open("Presets/Islands/%s" % ilha) as arquivoTxt:
                matrixIlha = [linha.split() for linha in arquivoTxt]

            # Inicializa e da append num novo objeto de ilha baseada nas informações do txt (Matrix,TamanhoX,TamanhoY)
            self.listaDeIlhas.append(IslInf.IslandsInfo(matrixIlha,len(matrixIlha),len(matrixIlha[0])))

        for obj in self.listaDeIlhas:
            print(obj)


    def popularMapa(self):

        frase = ""

        MaxTamanhoIlha = [0,0]

        for ilha in self.listaDeIlhas:
            if ilha.tamanhoXilha > MaxTamanhoIlha[0]:
                MaxTamanhoIlha[0] = ilha.tamanhoXilha

            if ilha.tamanhoYilha > MaxTamanhoIlha[1]:
                MaxTamanhoIlha[1] = ilha.tamanhoYilha

        print(MaxTamanhoIlha)


        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[0])):

                if self.mapa[i][j] == '_':

                    MaxXespaco = 0
                    MaxYespaco = 0

                    PodeDireita = True
                    PodeBaixo = True

                    while(PodeDireita):
                        # Verifica se não vai dar ArrayOutOfRange, Se o espaço não é maior do que a maior ilha
                        # e se o espaço subsequente está em branco
                        if (j + MaxXespaco < len(self.mapa[0]) and MaxXespaco < MaxTamanhoIlha[1]) and\
                                self.mapa[i][j + MaxXespaco] == '_':

                            MaxXespaco += 1

                        else: PodeDireita = False

                    while (PodeBaixo):
                        # Verifica se não vai dar ArrayOutOfRange, Se o espaço não é maior do que a maior ilha
                        # e se o espaço subsequente está em branco
                        if (i + MaxYespaco < len(self.mapa) and MaxYespaco < MaxTamanhoIlha[0]) and\
                                self.mapa[i + MaxYespaco][j] == '_':

                            MaxYespaco += 1

                        else:
                            PodeBaixo = False

                    random.shuffle(self.listaDeIlhas)

                    for ilha in self.listaDeIlhas:
                        if ilha.tamanhoXilha<=MaxYespaco and ilha.tamanhoYilha<=MaxXespaco:
                            for iIlha in range(len(ilha.matrixIlha)):
                                for jIlha in range(len(ilha.matrixIlha[0])):
                                    self.mapa[i+iIlha][j+jIlha] = ilha.matrixIlha[iIlha][jIlha]
                            break

                frase += "%s " % (self.mapa[i][j])
            frase += "\n"
        print(frase)
