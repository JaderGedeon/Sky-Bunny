import src.TileInfo as TileInfo
import random
import pygame as pg

class Textura:
    def __init__(self, idTextura, formatoTextura, tipoTextura, caminhoTextura, nomeTextura):

        self.idTextura = idTextura
        self.formatoTextura = formatoTextura
        self.tipoTextura = tipoTextura
        self.caminhoTextura = caminhoTextura
        self.nomeTextura = nomeTextura

class TexturasMapa:

    tamanhoTexturas = 6
    listaDeTexturas = []

    def __init__(self):

        #
        #
        #
        #
        #
        #                                ID   Formato     Tipo            Caminho do arquivo                        Descrição
        self.listaDeTexturas = [Textura(000, ["Centro"], "Céu", self.carregarImagem("texturas/tiles/Ceu.png"), "Quadrado de céu"),
                                Textura(1, ["Centro"], "Portal", self.carregarImagem("texturas/tiles/Portal.png"), "Portal por onde o personagem passa"),

                                Textura(100, ["Centro"], "Grama",self.carregarImagem("texturas/tiles/grama/Grama.png"),"Quadrado de grama"),
                                Textura(101, ["Centro"], "Grama", self.carregarImagem("texturas/tiles/grama/Grama1.png"), "Quadrado de grama com matinhos"),
                                Textura(102, ["Centro"], "Grama", self.carregarImagem("texturas/tiles/grama/Grama2.png"), "Quadrado de grama com folinhas"),
                                Textura(103, ["Esquerda"], "Grama", self.carregarImagem("texturas/tiles/grama/GramaLadoEsquerdo.png"),"Grama do lado esquerdo da ilha"),
                                Textura(104, ["Direita"], "Grama", self.carregarImagem("texturas/tiles/grama/GramaLadoDireito.png"), "Grama do lado direito da ilha"),
                                Textura(105, ["Cima"], "Grama", self.carregarImagem("texturas/tiles/grama/GramaLadoCima.png"), "Grama de cima da ilha"),
                                Textura(106, ["Baixo"], "Grama", self.carregarImagem("texturas/tiles/grama/GramaLadoBaixo.png"), "Grama da parte de baixo da ilha"),
                                Textura(107, ["CantoID"], "Grama", self.carregarImagem("texturas/tiles/grama/GramaCantoInferiorDireito.png"), "Grama do canto inferior direito"),
                                Textura(108, ["CantoIE"], "Grama", self.carregarImagem("texturas/tiles/grama/GramaCantoInferiorEsquerdo.png"), "Grama do canto inferior esquerdo"),
                                Textura(109, ["CantoSD"], "Grama", self.carregarImagem("texturas/tiles/grama/GramaCantoSuperiorDireito.png"), "Grama do canto superior direito"),
                                Textura(110, ["CantoSE"], "Grama", self.carregarImagem("texturas/tiles/grama/GramaCantoSuperiorEsquerdo.png"), "Grama do canto superior esquerdo"),
                                Textura(111, ["LigacaoID"], "Grama", self.carregarImagem("texturas/tiles/grama/GramaLigacaoInferiorDireita.png"), "Grama que liga o canto inferior com o direito"),
                                Textura(112, ["LigacaoIE"], "Grama", self.carregarImagem("texturas/tiles/grama/GramaLigacaoInferiorEsquerda.png"), "Grama que liga o canto inferior com o esquerdo"),
                                Textura(113, ["LigacaoSD"], "Grama", self.carregarImagem("texturas/tiles/grama/GramaLigacaoSuperiorDireita.png"), "Grama que liga o canto direito com o direito"),
                                Textura(114, ["LigacaoSE"], "Grama", self.carregarImagem("texturas/tiles/grama/GramaLigacaoSuperiorEsquerda.png"), "Grama que liga o canto direito com o esquerdo"),
                                #Textura(115, ["Centro"], "Grama", self.carregarImagem(""), ""),

                                Textura(200, ["Centro","Esquerda","Direita","Cima","Baixo"], "Ruina", self.carregarImagem("texturas/tiles/ruina/Ruina.png"), "Quadrado de ruina"),
                                Textura(205, ["CantoID", "LigacaoSE"], "Ruina", self.carregarImagem("texturas/tiles/ruina/RuinaCantoInferiorDireito.png"), "Ruina do canto inferior direito e tambem a ligacao"),
                                Textura(206, ["CantoIE", "LigacaoSD"], "Ruina", self.carregarImagem("texturas/tiles/ruina/RuinaCantoInferiorEsquerdo.png"), "Ruina do canto inferior esquerdo e tambem a ligacao"),
                                Textura(207, ["CantoSD", "LigacaoIE"], "Ruina", self.carregarImagem("texturas/tiles/ruina/RuinaCantoSuperiorDireito.png"), "Ruina do canto superior direito e tambem a ligacao"),
                                Textura(208, ["CantoSE", "LigacaoID"], "Ruina", self.carregarImagem("texturas/tiles/ruina/RuinaCantoSuperiorEsquerdo.png"), "Ruina do canto superior direito e tambem a ligacao"),

                                Textura(300, ["Centro"], "Parede", self.carregarImagem("texturas/tiles/Parede.png"), "Parede da ruína"),
                                #Textura(100, ["Centro"], "Grama", self.carregarImagem(""), ""),
                                ]

    def carregarImagem(self,caminho):
        return pg.transform.scale(pg.image.load(caminho), (self.tamanhoTexturas, self.tamanhoTexturas))

    def TexturizarTile(self, tile):
        random.shuffle(self.listaDeTexturas)
        for texturas in self.listaDeTexturas:
            if tile.formatoTile in texturas.formatoTextura and tile.tipoTerrenoTile == texturas.tipoTextura:
                return texturas.caminhoTextura

