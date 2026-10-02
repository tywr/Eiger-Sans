from draw.loop import draw_loop
from glyphs.lowercase.round import RoundLowercaseGlyph


class LowercaseOGlyph(RoundLowercaseGlyph):
    name = "lowercase_o"
    unicode = "0x6F"
    sbl = 0.627738
    sbr = 0.627738
    width_ratio = 1.002810
    bold_width_ratio = 1.096860
    bold_sbl = 0.614669
    bold_sbr = 0.599754

    def draw(
        self,
        pen,
        dc,
    ):
        b = self.body_bounds(dc)
        sx, sy = self.stroke_x_ratio * dc.stroke_x, self.stroke_y_ratio * dc.stroke_y
        draw_loop(pen, sx, sy, b.x1, b.y1, b.x2, b.y2, b.hx, b.hy)
