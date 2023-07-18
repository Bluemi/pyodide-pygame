from pyodide.ffi import to_js


class RightAttribute:
    def __get__(self, rect, obj_type=None):
        return rect.coordinates[0] + rect.coordinates[2]


class BottomAttribute:
    def __get__(self, rect, obj_type=None):
        return rect.coordinates[1] + rect.coordinates[3]


class Rect:
    right = RightAttribute()
    bottom = BottomAttribute()

    def __init__(self, left, top=None, width=None, height=None):
        if (width is None) != (height is None):
            raise ValueError("Variables width and height for rect are not equal")

        if top is None:
            left, top, width, height = left
        elif width is None:
            left, top, width, height = (left[0], left[1], top[0], top[1])

        self.left = left
        self.width = width
        self.top = top
        self.height = height

    def to_js(self):
        return to_js((self.left, self.top, self.width, self.height))

    def move(self, pos):
        return Rect(
            self.left + pos[0],
            self.top + pos[1],
            self.width,
            self.height,
        )
