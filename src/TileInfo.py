import pygame, time

class Tile(pygame.sprite.Sprite):
    def __init__(self, tipoTerrenoTile,formatoTile,texturaDoTile, idIlha, xTile, yTile):
        pygame.sprite.Sprite.__init__(self)

        # Tipo: Céu, Grama, Ruína
        # Formato: Canto Direito, Canto Inferior
        # Textura: Grama.png, Ruína.png
        # ID: Id da ilha pertencente, Céu = 0

        self.tipoTerrenoTile = tipoTerrenoTile
        self.formatoTile = formatoTile
        self.texturaDoTile = texturaDoTile
        self.idIlha = idIlha
        self.xTile = xTile
        self.yTile = yTile

    def desenho(self):
        self.image = self.texturaDoTile
        self.rect = self.image.get_rect()
        self.rect.x = self.xTile
        self.rect.y = self.yTile