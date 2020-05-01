import os
import src.IslandInfo as IslInf
import random

# Cada unidade de medida se refere a um Tile

class MapGenerator:
    mapa = []
    listaDeIlhas = []

    dimensoesIlha = {
        "maiorComprimento": 0,
        "maiorAltura": 0,

        "menorComprimento": 0,
        "menorAltura": 0
    }

    def __init__(self, comprimento, altura):
        self.comprimento = comprimento
        self.altura = altura

        # Cria um mapa com tamanho X e Y baseados nos valores de inicialização
        self.mapa = [['_' for x in range(comprimento)] for y in range(altura)]

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

            elif len(matrixIlha[0]) < self.dimensoesIlha["menorComprimento"] or self.dimensoesIlha["menorComprimento"] == 0:
                self.dimensoesIlha["menorComprimento"] = len(matrixIlha[0])

            if len(matrixIlha) > self.dimensoesIlha["maiorAltura"]:
                self.dimensoesIlha["maiorAltura"] = len(matrixIlha)

            elif len(matrixIlha) < self.dimensoesIlha["menorAltura"] or self.dimensoesIlha["menorAltura"] == 0:
                self.dimensoesIlha["menorAltura"] = len(matrixIlha)


            # Inicializa e da append num novo objeto de ilha baseada nas informações do txt (Matrix,TamanhoX,TamanhoY)
            self.listaDeIlhas.append(IslInf.IslandsInfo(matrixIlha,len(matrixIlha[0]),len(matrixIlha)))

    def popularMapa(self):

        frase = ""

        # Da o full scan no mapa para começar a populá-lo
        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[0])):

                if self.mapa[i][j] == '_':

                    espacoLivre = {
                        "comprimento": 0,
                        "altura": 0
                    }

                    # Verifica se não vai dar ArrayOutOfRange
                    # Se o espaço livre não é maior do que a maior ilha
                    # E se o espaço subsequente está em branco

                    while j + espacoLivre["comprimento"] < len(self.mapa[0]) and\
                            espacoLivre["comprimento"] < self.dimensoesIlha["maiorComprimento"] and\
                            self.mapa[i][j + espacoLivre["comprimento"]] == '_':

                        espacoLivre["comprimento"] += 1

                    while i + espacoLivre["altura"] < len(self.mapa) and\
                            espacoLivre["altura"] < self.dimensoesIlha["maiorAltura"] and\
                            self.mapa[i + espacoLivre["altura"]][j] == '_':

                        espacoLivre["altura"] += 1


                    random.shuffle(self.listaDeIlhas)

                    # Procura a primeira ilha no array de ilhas que encaixe no espaço livre
                    for ilha in self.listaDeIlhas:
                        if ilha.comprimentoIlha <= espacoLivre["comprimento"] and ilha.alturaIlha <= espacoLivre["altura"]:
                            #Caso for adicionar algo para saber qual é cada ilha, adicionar aqui!
                            for iIlha in range(ilha.alturaIlha):
                                for jIlha in range(ilha.comprimentoIlha):
                                    self.mapa[i+iIlha][j+jIlha] = ilha.matrixIlha[iIlha][jIlha]

                            break

                    # Caso não tenha conseguido preencher com uma ilha, troca pra céu
                    if self.mapa[i][j] == '_':
                        self.mapa[i][j] = '.'


                frase += "%s " % (self.mapa[i][j])
            frase += "\n"
        print(frase)

    def reiniciarMapa(self):
        self.mapa = [['_' for x in range(self.comprimento)] for y in range(self.altura)]
        MapGenerator.popularMapa(self)
