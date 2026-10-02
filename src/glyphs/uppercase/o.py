from glyphs.uppercase import UppercaseGlyph
from draw.loop import draw_loop


class UppercaseOGlyph(UppercaseGlyph):
    name = "uppercase_o"
    unicode = "0x4F"
    stroke_x_ratio = UppercaseGlyph.stroke_x_ratio * 1.05
    stroke_y_ratio = UppercaseGlyph.stroke_y_ratio * 1.02
    width_ratio = 1.335702
    bold_width_ratio = 1.402521
    sbl = 0.744047
    sbr = 0.744047
    overshoot_bottom = True
    overshoot_top = True
    bold_sbl = 0.741653
    bold_sbr = 0.733443

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        draw_loop(
            pen,
            dc.stroke_x * self.stroke_x_ratio,
            dc.stroke_y * self.stroke_y_ratio,
            b.x1,
            b.y1,
            b.x2,
            b.y2,
            b.hx,
            b.hy,
        )
