class Entity:
    def __init__(self,image, rect, rectx,recty,largeur,hauteur,speed = None):
        self.image = image
        self.rect = rect
        self.rectx = rectx
        self.recty = recty
        self.largeur = largeur
        self.hauteur = hauteur
        self.speed = speed