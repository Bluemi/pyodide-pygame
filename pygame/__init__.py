from . import display
from . import draw
from . import event
from . import font
from . import mouse
from . import key
from .rect import *




class Color:
    class ColorIterator:
        def __init__(self, c):
            self.color = c
            self.position = 0

        def __next__(self):
            position = self.position
            self.position += 1
            if position >= 3:
                raise StopIteration()
            return (self.color.r, self.color.g, self.color.b)[position]

    def __init__(self, r, g=None, b=None, a=255):
        if (g is None) and (b is None):
            r, g, b = r
        else:
            r = r
            g = g
            b = b
        a = a

        self.r = int(r)
        self.g = int(g)
        self.b = int(b)
        self.a = int(a)

    def __sub__(self, other):
        return Color(self.r - other.r, self.g - other.g, self.b - other.b, self.a)

    def __repr__(self):
        return 'Color(r={} g={} b={} a={})'.format(self.r, self.g, self.b, self.a)

    def __iter__(self):
        return Color.ColorIterator(self)


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

    def set_alpha(self, _alpha):
        # print('setting alpha for Surface is not supported')
        pass


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
WINDOWFOCUSGAINED = event.WINDOWFOCUSGAINED
FOCUS = event.FOCUS
QUIT = event.QUIT
WINDOWSHOWN = event.WINDOWSHOWN
TEXTINPUT = event.TEXTINPUT

# MOD CODES
KMOD_SHIFT = 1
KMOD_LSHIFT = 2