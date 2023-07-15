import pygame_helper
import pyodide.ffi


class Screen:
    def __init__(self, canvas):
        self.canvas = canvas

    def fill(self, color):
        pygame_helper.display.fill(self.canvas, pyodide.ffi.to_js(color))


def set_mode(screen_size):
    return Screen(pygame_helper.display.set_mode(pyodide.ffi.to_js(screen_size)))


def flip():
    pass

