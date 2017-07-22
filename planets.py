import pygame
import math

class BaseObject(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super(BaseObject, self).__init__()

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.position = position
        self.rect.center = position

    def manejar_click(self, x, y):
        if self.rect.collidepoint(x, y):
            self.rect.center = self.rect.center[0] + 10, self.rect.center[1] + 10



class Planet(BaseObject):
    def __init__(self, image, sun_position, distance_from_sun):
        position = (sun_position[0] + distance_from_sun, sun_position[1] + distance_from_sun)

        super(Planet, self).__init__(image, position)
        self.sun_position = sun_position
        self.r = distance_from_sun
        self.angulo = 0

    def update(self, *args):
        """
        Generar coordenadas que definen una orbita eliptica.
        """
        x = self.sun_position[0] + (self.r * math.cos(math.radians(self.angulo)))
        y = self.sun_position[1] + ((self.r * 0.5) * math.sin(math.radians(self.angulo)))

        self.angulo += 1
        if self.angulo >= 360:
            self.angulo = 1
        self.rect.center = (x, y)
