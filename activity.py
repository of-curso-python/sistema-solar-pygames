import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


import sugar3.activity.activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.graphics.toolbutton import ToolButton
from sugar3.activity.widgets import StopButton

from sugargame import canvas

from sistema_solar import JuegoSistemaSolar


class JuegoSistemaSolarActivity(sugar3.activity.activity.Activity):
    def __init__(self, handle):
        super(JuegoSistemaSolarActivity, self).__init__(handle)

        self.build_toolbar()

        # Crear instancia de Juego.
        self.game = JuegoSistemaSolar()
        self.paused = False

        # Crear Pygame canvas.
        self._pygamecanvas = canvas.PygameCanvas(self)
        self.set_canvas(self._pygamecanvas)
        self._pygamecanvas.grab_focus()
        self._pygamecanvas.run_pygame(self.game.run)

    def build_toolbar(self):
        toolbar_box = ToolbarBox()
        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

        activity_button = ActivityToolbarButton(self)
        toolbar_box.toolbar.insert(activity_button, -1)
        activity_button.show()

        # Pause/Play button:
        stop_play = ToolButton('media-playback-stop')
        stop_play.set_tooltip("Alto")
        stop_play.set_accelerator('<ctrl>space')
        stop_play.connect('clicked', self.pausar)
        stop_play.show()

        toolbar_box.toolbar.insert(stop_play, -1)

        # Blank space (separator) and Stop button at the end:

        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()

    def pausar(self, button):
        # Detener o resumir juego.
        self.paused = not self.paused
        self.game.set_paused(self.paused)

        # Actualizar el icono del boton iniciar/pausar.
        if self.paused:
            button.set_icon('media-playback-start')
            button.set_tooltip("Start")
        else:
            button.set_icon('media-playback-stop')
            button.set_tooltip("Stop")

    def read_file(self, file_path):
        self.game.read_file(file_path)

    def write_file(self, file_path):
        self.game.write_file(file_path)
