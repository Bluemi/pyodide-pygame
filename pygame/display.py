import pygame_helper
from pyodide.ffi import to_js

from .rect import Rect
from .draw import rect, _DrawInstruction


window_size = (0, 0)


class Screen:
    def __init__(self, canvas, size):
        self.canvas = canvas
        self.size = size

    def fill(self, color):
        pygame_helper.display.fill(self.canvas, to_js(color))

    def blit(self, render_object, position):
        if render_object.get_surface_type() == 'RenderFont':
            font_style = "{}px sans-serif".format(render_object.font.fontsize)
            pygame_helper.draw.font(
                self.canvas,
                to_js(render_object.color),
                to_js(position),
                font_style,
                render_object.text,
                # render_object.antialias,  # ignore these parameters
                # to_js(render_object.background)
            )
        elif render_object.get_surface_type() == 'Surface':
            for instruction in render_object.draw_instructions:
                if instruction.draw_type == _DrawInstruction.FILL:
                    rect_pos = Rect(position[0], position[1], render_object.size[0], render_object.size[1])
                    rect(self, instruction.color, rect_pos, 0)
                elif instruction.draw_type == _DrawInstruction.RECT:
                    rect_pos = instruction.rect_pos.move(position)
                    rect(self, instruction.color, rect_pos, instruction.border_radius)
        else:
            raise NotImplementedError('blit {} on screen not supported'.format(render_object.get_surface_type()))

    def get_surface_type(self):
        return 'Screen'

    def get_width(self):
        return self.size[0]

    def get_height(self):
        return self.size[1]


def set_mode(screen_size):
    global window_size
    window_size = screen_size
    return Screen(pygame_helper.display.set_mode(to_js(screen_size)), screen_size)


def flip():
    pass


def get_window_size():
    return window_size
