from . import display
from . import draw
from . import event
from . import font
from . import mouse
from .rect import *


class Color:
    def __init__(self, r, g, b, a=255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __sub__(self, other):
        return Color(self.r - other.r, self.g - other.g, self.b - other.b, self.a)


class Surface:
    def __init__(self, size):
        self.size = size
        self.draw_instructions = []

    def fill(self, color):
        fill_instruction = draw._DrawInstruction(draw._DrawInstruction.FILL, color=color)
        self.draw_instructions.append(fill_instruction)

    def get_width(self):
        return self.size[0]

    def get_height(self):
        return self.size[1]

    def blit(self, surface, rect):
        raise NotImplementedError('Surface.blit() currently not implemented')

    def get_surface_type(self):
        return 'Surface'


def init():
    pass


def quit():
    pass


# event types
MOUSEBUTTONDOWN = event.MOUSEBUTTONDOWN
MOUSEBUTTONUP = event.MOUSEBUTTONUP
MOUSEENTER = event.MOUSEENTER
MOUSEMOTION = event.MOUSEMOTION
MOUSEWHEEL = event.MOUSEWHEEL
KEYDOWN = event.KEYDOWN
KEYUP = event.KEYUP
WINDOWRESIZED = event.WINDOWRESIZED
WINDOWENTER = event.WINDOWENTER
FOCUS = event.FOCUS
QUIT = event.QUIT
