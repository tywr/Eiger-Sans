from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm


class LowercaseXGlyph(Glyph):
    name = "lowercase_x"
    unicode = "0x78"
    stroke_ratio = 1.1
    width_ratio = 1.002
    bold_width_ratio = 1.123
    top_offset = 0.02
    sbl = 0.159
    sbr = 0.159
    bold_sbl = 0.014
    bold_sbr = 0.014

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx = self.diag_stroke_dampening(self.stroke_ratio, dc.stroke_x, coef=0.0)
        x1t = b.x1 + self.top_offset * b.width
        x2t = b.x2 - self.top_offset * b.width
        draw_parallelogramm(
            pen, dc.stroke_x, dc.stroke_y, b.x1, b.y1, x2t, b.y2, delta=sx
        )
        theta, delta = draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x2,
            b.y1,
            x1t,
            b.y2,
            direction="top-left",
            delta=sx,
        )
