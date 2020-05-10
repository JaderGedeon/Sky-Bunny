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

    tamanhoTexturas = 32
    listaDeTexturas = []

    def __init__(self):

        #
        #
        #
        #
        #
        #
        #

        self.listaDeTexturas = [Textura(000,"Centro","Céu",self.carregarImagem("textures/Ceu.png"),"Quadrado de céu"),

                                Textura(100,"Centro","Grama",self.carregarImagem("textures/grass/Grama.png"),"Quadrado de grama"),
                                Textura(101, "Centro", "Grama", self.carregarImagem("textures/grass/Grama1.png"), "Quadrado de grama com matinhos"),
                                Textura(102, "Centro", "Grama", self.carregarImagem("textures/grass/Grama2.png"), "Quadrado de grama com folinhas"),
                                Textura(103, "Esquerda", "Grama", self.carregarImagem("textures/grass/GramaLadoEsquerdo.png"),"Grama do lado esquerdo da ilha"),
                                Textura(104, "Direita", "Grama", self.carregarImagem("textures/grass/GramaLadoDireito.png"), "Grama do lado direito da ilha"),
                                Textura(105, "Cima", "Grama", self.carregarImagem("textures/grass/GramaLadoCima.png"), "Grama de cima da ilha"),
                                Textura(106, "Baixo", "Grama", self.carregarImagem("textures/grass/GramaLadoBaixo.png"), "Grama da parte de baixo da ilha"),
                                Textura(107, "CantoID", "Grama", self.carregarImagem("textures/grass/GramaCantoInferiorDireito.png"), "Grama do canto inferior direito"),
                                Textura(108, "CantoIE", "Grama", self.carregarImagem("textures/grass/GramaCantoInferiorEsquerdo.png"), "Grama do canto inferior esquerdo"),
                                Textura(109, "CantoSD", "Grama", self.carregarImagem("textures/grass/GramaCantoSuperiorDireito.png"), "Grama do canto superior direito"),
                                Textura(110, "CantoSE", "Grama", self.carregarImagem("textures/grass/GramaCantoSuperiorEsquerdo.png"), "Grama do canto superior esquerdo"),
                                Textura(111, "LigacaoID", "Grama", self.carregarImagem("textures/grass/GramaLigacaoInferiorDireita.png"), "Grama que liga o canto inferior com o direito"),
                                Textura(112, "LigacaoIE", "Grama", self.carregarImagem("textures/grass/GramaLigacaoInferiorEsquerda.png"), "Grama que liga o canto inferior com o esquerdo"),
                                Textura(113, "LigacaoSD", "Grama", self.carregarImagem("textures/grass/GramaLigacaoSuperiorDireita.png"), "Grama que liga o canto direito com o direito"),
                                Textura(114, "LigacaoSE", "Grama", self.carregarImagem("textures/grass/GramaLigacaoSuperiorEsquerda.png"), "Grama que liga o canto direito com o esquerdo"),
                                #Textura(110, "Centro", "Grama", self.carregarImagem(""), ""),

                                #Textura(100, "Centro", "Grama", self.carregarImagem(""), ""),
                                ]

    def carregarImagem(self,caminho):
        return pg.transform.scale(pg.image.load(caminho), (self.tamanhoTexturas, self.tamanhoTexturas))

    def TexturizarTile(self, tile):
        random.shuffle(self.listaDeTexturas)
        for texturas in self.listaDeTexturas:
            if tile.formatoTile == texturas.formatoTextura and tile.tipoTerrenoTile == texturas.tipoTextura:
                return texturas.caminhoTextura

