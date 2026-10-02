from glyphs import Glyph
from draw.rect import draw_rect


class LowercaseLGlyph(Glyph):
    name = "lowercase_l"
    unicode = "0x6C"
    stroke_x_ratio = 0.999647
    bold_width_ratio = 0.294
    width_ratio = 0.177366
    sbl = 0.999762
    sbr = 0.999762
    bold_sbl = 1.000
    bold_sbr = 1.000

    def window_width(self, dc):
        return (
            dc.stroke_x * self.stroke_x_ratio
            + (self.adjusted_sbl(dc) + self.adjusted_sbr(dc)) * dc.side_bearing
        )

    def body_bounds(self, dc):
        return dc.body_bounds(
            width=dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.adjusted_sbr(dc) * dc.side_bearing,
            side_bearing_left=self.adjusted_sbl(dc) * dc.side_bearing,
            height=self.height,
            number=self.number,
            uppercase=self.uppercase,
            overshoot_bottom=self.overshoot_bottom,
            overshoot_top=self.overshoot_top,
        )

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        # Stem
        sx = dc.stroke_x * self.stroke_x_ratio
        draw_rect(pen, b.xmid - sx / 2, 0, b.xmid + sx / 2, dc.ascent)
