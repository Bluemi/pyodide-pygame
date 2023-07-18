class _RenderedFont:
    def __init__(self, font, text, antialias, color, background):
        self.font = font
        self.text = text
        self.antialias = antialias
        self.color = color
        self.background = background

    def get_surface_type(self):
        return 'RenderFont'

    def get_width(self):
        return self.font.fontsize * len(self.text) * 0.6

    def get_height(self):
        return self.font.fontsize * 1.2


class Font:
    def __init__(self, fontname, fontsize):
        self.fontname = fontname
        self.fontsize = fontsize

    def render(self, text, antialias, color, background=None):
        return _RenderedFont(self, text, antialias, color, background)


def get_default_font():
    return "freesansbold.ttf"
