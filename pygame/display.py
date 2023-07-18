import pygame_helper
from pyodide.ffi import to_js
from .font import _RenderedFont


class Screen:
    def __init__(self, canvas):
        self.canvas = canvas

    def fill(self, color):
        pygame_helper.display.fill(self.canvas, to_js(color))

    def blit(self, render_object, position):
        if isinstance(render_object, _RenderedFont):
            # font_style = "{}px {}".format(render_object.font.fontsize, render_object.font.fontname)
            font_style = "{}px serif".format(render_object.font.fontsize)
            pygame_helper.draw.font(
                self.canvas,
                to_js(render_object.color),
                to_js(position),
                font_style,
                render_object.text,
                # render_object.antialias,  # ignore these parameters
                # to_js(render_object.background)
            )


def set_mode(screen_size):
    return Screen(pygame_helper.display.set_mode(to_js(screen_size)))


def flip():
    pass

