import pygame_helper
from pyodide.ffi import to_js

from .rect import Rect


def line(screen, color, start, dest):
    if screen.get_surface_type() == 'Screen':
        pygame_helper.draw.line(screen.canvas, to_js(color), to_js(start), to_js(list(dest)))
    else:
        raise NotImplementedError('Drawing line on {} not supported'.format(screen.get_surface_type()))


def circle(screen, color, center, radius):
    if screen.get_surface_type() == 'Screen':
        pygame_helper.draw.circle(screen.canvas, to_js(color), to_js(center), radius)
    else:
        raise NotImplementedError('Drawing circle on {} not supported'.format(screen.get_surface_type()))


def rect(screen, color, rect_pos, border_radius=0):
    if isinstance(rect_pos, tuple):
        rect_pos = Rect(rect_pos)

    if screen.get_surface_type() == 'Screen':
        pygame_helper.draw.rect(screen.canvas, to_js(color), rect_pos.to_js(), border_radius)
    elif screen.get_surface_type() == 'Surface':
        instruction = _DrawInstruction(
            _DrawInstruction.RECT, color=color, rect_pos=rect_pos, border_radius=border_radius
        )
        screen.draw_instructions.append(instruction)
    elif screen.get_surface_type() == 'SubScreen':
        rect_pos = rect_pos.move(screen.subrect.lefttop)
        pygame_helper.draw.rect(screen.canvas, to_js(color), rect_pos.to_js(), border_radius)
    else:
        raise NotImplementedError('Drawing rect on {} not supported'.format(screen.get_surface_type()))


class _DrawInstruction:
    FILL = 0
    RECT = 1

    def __init__(self, draw_type, color=None, rect_pos=None, border_radius=None):
        self.draw_type = draw_type
        self.color = color
        self.rect_pos = rect_pos
        self.border_radius = border_radius
