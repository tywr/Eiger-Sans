from abc import ABC, abstractmethod
from glyphs import Glyph

from draw.rect import draw_rect


class DottedLowercaseGlyph(Glyph, ABC):
    """Define common class variables for single-story lowercase glyphs"""

    dot_height = 1.1
    dot_width = 1.1
    bold_dot_width = 1.1
    dot_position = "xmid"
    min_opening = 85
    sbl = 1
    sbr = 1

    @abstractmethod
    def draw_base(self, pen, dc): ...

    def draw(self, pen, dc):
        self.draw_base(pen, dc)
        b = self.body_bounds(dc)
        if dc.weight <= 400:
            dot_width = self.dot_width
        else:
            blend = (dc.weight - 400) / 300
            dot_width = (1 - blend) * self.dot_width + blend * self.bold_dot_width
        w = dc.stroke_x * dot_width

        # Accent dot
        if self.dot_position == "x2":
            xpos = getattr(b, self.dot_position) - dc.stroke_x / 2
        elif self.dot_position == "x1":
            xpos = getattr(b, self.dot_position) + dc.stroke_x / 2
        else:
            xpos = getattr(b, self.dot_position)
        dh = self.dot_height * dc.stroke_x
        draw_rect(
            pen,
            xpos - w / 2,
            max(dc.ascent - dh, dc.x_height + self.min_opening),
            xpos + w / 2,
            dc.ascent,
        )
