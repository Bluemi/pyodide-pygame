import pygame_helper
from pyodide.ffi import to_js


def line(screen, color, start, dest):
    pygame_helper.draw.line(screen.canvas, to_js(color), to_js(start), to_js(list(dest)))


def circle(screen, color, center, radius):
    pygame_helper.draw.circle(screen.canvas, to_js(color), to_js(center), radius)


def rect(screen, color, rect_pos):
    pygame_helper.draw.rect(screen.canvas, to_js(color), to_js(rect_pos))
