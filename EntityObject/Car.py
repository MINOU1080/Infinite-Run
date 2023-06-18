import pygame as py

from EntityObject.EntityObject import Entity


class Car(Entity):
    def __init__(self, image, rect, rectx, recty, largeur, hauteur):
        super().__init__(image, rect, rectx, recty, largeur, hauteur)
        self.carPicture = py.image.load("Assets/picture/car.png")
        self.rect = self.carPicture.get_rect()  # donne les coords de notre image
        self.rect.x = 500
        self.rect.y = 600

        self.largeur = 50
        self.hauteur = 100
        self.speed = 3

        self.pressed = {}

    def drawPlayer(self, screen):
        self.carPicture = py.transform.scale(self.carPicture, (self.largeur, self.hauteur))
        screen.blit(self.carPicture, self.rect)

    def moveUp(self):
        self.rect.y -= self.speed

    def moveDown(self):
        self.rect.y += self.speed

    def moveLeft(self):
        self.rect.x -= self.speed

    def moveRight(self):
        self.rect.x += self.speed
