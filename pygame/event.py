from typing import Callable, Optional
from . import mouse


handle_events_callback: Optional[Callable] = None


def register_event_callback(handle_events):
    global handle_events_callback
    handle_events_callback = handle_events


def handle_event(evt):
    if handle_events_callback is not None:
        handle_events_callback([evt])
    if evt.type == MOUSEMOTION:
        mouse.mouse_position = evt.pos


class Event:
    def __init__(self, evt_type, pos=None, y=None, key=None, unicode=None, button=None):
        self.type = evt_type
        self.pos = pos
        self.y = y
        self.key = key
        self.unicode = unicode
        self.button = button

    @staticmethod
    def create_mousebuttondown(pos, button):
        return Event(MOUSEBUTTONDOWN, pos=pos, button=button)

    @staticmethod
    def create_mousebuttonup(pos, button):
        return Event(MOUSEBUTTONUP, pos=pos, button=button)

    @staticmethod
    def create_mouseenter():
        return Event(MOUSEENTER)

    @staticmethod
    def create_mousemotion(pos):
        return Event(MOUSEMOTION, pos=pos)

    @staticmethod
    def create_mousewheel(y):
        return Event(MOUSEWHEEL, y=y)

    @staticmethod
    def create_keydown(key, unicode):
        return Event(KEYDOWN, key=key, unicode=unicode)

    @staticmethod
    def create_keyup(key, unicode):
        return Event(KEYUP, key=key, unicode=unicode)

    @staticmethod
    def create_windowresized():
        return Event(WINDOWRESIZED)

    @staticmethod
    def create_focus():
        return Event(FOCUS)

    def __repr__(self):
        rpr = ["Event(type={}".format(_type_to_str(self.type))]
        if self.pos is not None:
            rpr.append("pos={}".format(self.pos))
        if self.y is not None:
            rpr.append("y={}".format(self.y))
        if self.key is not None:
            rpr.append("key={}".format(self.key))
        if self.unicode is not None:
            rpr.append("unicode={}".format(self.unicode))
        if self.button is not None:
            rpr.append("button={}".format(self.button))
        return '  '.join(rpr) + ')'

    # @staticmethod
    # def create_quit():
    #     return Event(QUIT)


MOUSEBUTTONDOWN = 0
MOUSEBUTTONUP = 1
MOUSEENTER = 2
MOUSEMOTION = 3
MOUSEWHEEL = 4
KEYDOWN = 5
KEYUP = 6
WINDOWRESIZED = 7
WINDOWENTER = 8
WINDOWFOCUSGAINED = 8
FOCUS = 9
QUIT = 10


def _type_to_str(t):
    if t == MOUSEBUTTONDOWN:
        return "MOUSEBUTTONDOWN"
    elif t == MOUSEBUTTONUP:
        return "MOUSEBUTTONUP"
    elif t == MOUSEENTER:
        return "MOUSEENTER"
    elif t == MOUSEMOTION:
        return "MOUSEMOTION"
    elif t == MOUSEWHEEL:
        return "MOUSEWHEEL"
    elif t == KEYDOWN:
        return "KEYDOWN"
    elif t == KEYUP:
        return "KEYUP"
    elif t == WINDOWRESIZED:
        return "WINDOWRESIZED"
    elif t == FOCUS:
        return "FOCUS"
    elif t == QUIT:
        return "QUIT"
    else:
        raise ValueError("Unknown event type: {}".format(t))

