from draw.arch import draw_arch
from draw.rect import draw_rect

from glyphs.lowercase.square import SquareLowercaseGlyph


class LowercaseHGlyph(SquareLowercaseGlyph):
    name = "lowercase_h"
    unicode = "0x68"
    width_ratio = 0.888802
    sbl = 0.999762
    sbr = 0.883571
    overshoot_top = True
    bold_width_ratio = 1.011859
    bold_sbl = 1.042282
    bold_sbr = 0.908730

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        yl = b.y2 - self.loop_ratio * b.height

        # Top arch, cut at the bottom (only upper half drawn)
        draw_arch(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            yl,
            b.x2,
            b.y2,
            self.hx_ratio * b.hx,
            self.hy_ratio * b.hy,
            taper=self.taper * dc.taper,
            side="left",
            cut="bottom",
        )
        draw_rect(pen, b.x1, 0, b.x1 + dc.stroke_x, dc.ascent)

        # Right stem — reaches up to the arch midpoint
        draw_rect(pen, b.x2 - dc.stroke_x, 0, b.x2, (b.y2 + yl) / 2)
