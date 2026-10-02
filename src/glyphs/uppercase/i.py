from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect


class UppercaseIGlyph(UppercaseGlyph):
    name = "uppercase_i"
    unicode = "0x49"
    stroke_x_ratio = 1.034118
    width_ratio = 0.189390
    sbl = 1.069524
    sbr = 1.069524
    bold_width_ratio = 0.316
    bold_sbl = 1.169
    bold_sbr = 1.169

    def window_width(self, dc):
        return (
            dc.stroke_x * self.stroke_x_ratio
            + (self.adjusted_sbr(dc) + self.adjusted_sbl(dc)) * dc.side_bearing
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
        sx = dc.stroke_x * self.stroke_x_ratio

        # Vertical stem (centered)
        draw_rect(pen, b.xmid - sx / 2, b.y1, b.xmid + sx / 2, b.y2)
