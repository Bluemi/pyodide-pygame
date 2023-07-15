import pygame_helper
import pyodide.ffi


def line(screen, color, start, dest):
    pygame_helper.draw.line(screen.canvas, pyodide.ffi.to_js(color), pyodide.ffi.to_js(start), pyodide.ffi.to_js(dest))

