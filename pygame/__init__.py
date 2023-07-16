from . import display
from . import draw
from . import event
from . import mouse


class Color:
    def __init__(self, r, g, b, a=255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a


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
FOCUS = event.FOCUS
QUIT = event.QUIT
