import pygame
import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

from planets import BaseObject, Planet

class JuegoSistemaSolar(object):
    def __init__(self):
        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()
        self.paused = False
        self.default_planet_img = 'img/planet-placeholder.png'

    def set_paused(self, paused):
        self.paused = paused

    # Called to save the state of the game to the Journal.
    def write_file(self, file_path):
        pass

    # Called to load the state of the game from the Journal.
    def read_file(self, file_path):
        pass

    # Bucle del juego.
    def run(self):
        self.running = True

        screen = pygame.display.get_surface()
        screen_rect = screen.get_rect()
        self.sun_position = (screen_rect.centerx, screen_rect.centery)

        planetas = self.crear_cuerpos_celestes()
        self.planet_sprite = pygame.sprite.RenderPlain(planetas)

        while self.running:
            # Pump GTK messages.
            while Gtk.events_pending():
                Gtk.main_iteration()

            # Pump PyGame messages.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.VIDEORESIZE:
                    pygame.display.set_mode(event.size, pygame.RESIZABLE)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.direction = -1
                    elif event.key == pygame.K_RIGHT:
                        self.direction = 1

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for planeta in planetas:
                        planeta.manejar_click(*event.pos)

            # Pinta la pantalla en negro en cada iteracion.
            screen.fill((0, 0, 0))
            self.clock.tick(30)


            if not self.paused:
                self.planet_sprite.update()

            self.planet_sprite.draw(screen)
            # Esto redibuja/actualiza la pantalla.
            pygame.display.flip()

    def crear_cuerpos_celestes(self):
        sun = BaseObject(
            self.default_planet_img,
            self.sun_position
        )

        planetas = [
            sun,
            Planet(
                self.default_planet_img,
                self.sun_position,
                250
            ),
            Planet(
                self.default_planet_img,
                self.sun_position,
                500
            ),
        ]

        return planetas



if __name__ == '__main__':
    # Esto ejecuta el juego directamente desde la terminal.
    pygame.init()
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = JuegoSistemaSolar()
    game.run()
