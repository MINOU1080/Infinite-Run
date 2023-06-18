import pygame as py

from EntityObject.EntityObject import Entity


class FireBall(Entity):
    def __init__(self, voiture, image, rect, rectx, recty, largeur, hauteur):
        super().__init__(image, rect, rectx, recty, largeur, hauteur)
        self.fireball = py.image.load("Assets/picture/bouledefeu.png")
        self.largeur = 50
        self.hauteur = 90

        self.rect = self.fireball.get_rect()
        self.rect.x = voiture.rect.x
        self.rect.y = voiture.rect.y - 100
        self.speed = 10

    def draw(self, screen):
        self.fireball = py.transform.scale(self.fireball, (self.largeur, self.hauteur))
        screen.blit(self.fireball, self.rect)  # place l'image

    def update(self):
        self.rect.y -= self.speed

    def __repr__(self):
        return 'fireba'
