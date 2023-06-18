import pygame as py
from EntityObject.Car import Car
from EntityObject.FireBall import FireBall


class BoardPygame:
    def __init__(self, screen):
        self.screen = screen
        self.image = py.image.load("Assets/picture/background.jpg")
        self.voiture = Car()

        self.fondx = 0
        self.fondy = 0
        self.speedScreen = 2

        self.fireballs = []

        self.clock = py.time.Clock()

    def getEvent(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()

            elif event.type == py.KEYDOWN:
                self.voiture.pressed[event.key] = True

                if self.voiture.pressed.get(py.K_SPACE):
                    fire = FireBall(self.voiture)
                    self.fireballs.append(fire)

            elif event.type == py.KEYUP:
                self.voiture.pressed[event.key] = False

    def update(self):
        if self.voiture.pressed.get(py.K_RIGHT) and self.voiture.rect.x < 1000:
            self.voiture.moveRight()

        elif self.voiture.pressed.get(py.K_LEFT) and self.voiture.rect.x > 10:
            self.voiture.moveLeft()

        elif self.voiture.pressed.get(py.K_UP) and self.voiture.rect.y > 10:
            self.voiture.moveUp()

        elif self.voiture.pressed.get(py.K_DOWN) and self.voiture.rect.y < 610:
            self.voiture.moveDown()

    def display(self):
        self.fondy -= self.speedScreen
        self.clock.tick(60)
        py.display.flip()  # maj ecran

        self.screen.blit(self.image, (self.fondx, self.fondy))  # Place le fond
        self.screen.blit(self.image, (self.fondx, self.fondy + 720)) #faire defiler le le fond

        if self.fondy <= -720:
            self.fondy = 0

        for fireb in self.fireballs:
            fireb.update()
            fireb.draw(self.screen)

        self.voiture.drawPlayer(self.screen)

    def run(self):
        while True:
            self.getEvent()

            self.update()

            # Supprimez les boules de feu qui ont atteint la limite de l'écran
            self.fireballs = [fireball for fireball in self.fireballs if fireball.rect.y > -fireball.hauteur]

            self.display()

