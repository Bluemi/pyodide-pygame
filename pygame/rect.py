from pyodide.ffi import to_js


class RightAttribute:
    def __get__(self, rect, obj_type=None):
        return rect.left + rect.width


class BottomAttribute:
    def __get__(self, rect, obj_type=None):
        return rect.top + rect.height


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

    def __getitem__(self, index):
        return (self.left, self.top, self.width, self.height)[index]

    def to_js(self):
        return to_js((self.left, self.top, self.width, self.height))

    def move(self, pos):
        return Rect(
            self.left + pos[0],
            self.top + pos[1],
            self.width,
            self.height,
        )

    def copy(self):
        return Rect(self.left, self.top, self.width, self.height)

    def collidepoint(self, point):
        return self.left < point[0] < self.right and self.top < point[1] < self.bottom

    def clip(self, other):
        left = max(self.left, other.left)
        top = max(self.top, other.top)
        right = min(self.right, other.right)
        bottom = min(self.bottom, other.bottom)
        return Rect(left, top, right-left, bottom-top)
