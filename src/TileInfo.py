class Tile:
    def __init__(self, tipoTerrenoTile,formatoTile,texturaDoTile, idIlha):

        # Tipo: Céu, Grama, Ruína
        # Formato: Canto Direito, Canto Inferior
        # Textura: Grama.png, Ruína.png
        # ID: Id da ilha pertencente, Céu = 0

        self.tipoTerrenoTile = tipoTerrenoTile
        self.formatoTile = formatoTile
        self.texturaDoTile = texturaDoTile
        self.idIlha = idIlha