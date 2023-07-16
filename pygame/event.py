from typing import Callable, Optional


handle_events_callback: Optional[Callable] = None


def register_event_callback(handle_events):
    print('event callback registered')
    global handle_events_callback
    handle_events_callback = handle_events


def handle_event(evt):
    if handle_events_callback is not None:
        handle_events_callback([evt])


class Event:
    def __init__(self, evt_type):
        self.type = evt_type

    @staticmethod
    def create_click():
        return Event(MOUSEBUTTONDOWN)


MOUSEBUTTONDOWN = 0
QUIT = 1
KEYDOWN = 2
