import pyodide.ffi
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
    def __init__(self, evt_type, pos=None):
        self.type = evt_type
        self.pos = pos

    @staticmethod
    def create_click(pos):
        return Event(MOUSEBUTTONDOWN, pos=pos)

    @staticmethod
    def create_mousemotion(pos):
        return Event(MOUSEMOTION, pos=pos)


MOUSEBUTTONDOWN = 0
QUIT = 1
KEYDOWN = 2
MOUSEMOTION = 3
