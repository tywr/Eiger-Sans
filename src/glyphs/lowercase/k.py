from glyphs import Glyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm


class LowercaseKGlyph(Glyph):
    name = "lowercase_k"
    unicode = "0x6B"
    width_ratio = 0.905951
    bold_width_ratio = 1.047190
    mid_ratio = 0.565
    upper_branch_offset = 0.04
    stroke_x_ratio = 1.00
    branch_stroke_ratio = 1.3
    branch_overlap = 0.95
    sbl = 0.999762
    sbr = 0.244167
    bold_sbl = 1.042282
    bold_sbr = 0.253831

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx = self.stroke_x_ratio * dc.stroke_x
        xb = b.x1 + self.branch_overlap * sx
        sd = self.diag_stroke_dampening(self.branch_stroke_ratio, sx, coef=0.1)
        xtop = b.x2 - self.upper_branch_offset * b.width
        ymid = b.y1 + self.mid_ratio * b.height

        # Left ascender stem
        draw_rect(pen, b.x1, 0, b.x1 + sx, dc.ascent)

        # Lower branch
        draw_parallelogramm(
            pen,
            0,
            0,
            xb,
            ymid,
            b.x2,
            b.y1,
            direction="bottom-right",
            delta=sd,
        )

        # Upper branch
        theta, delta = draw_parallelogramm(
            pen,
            0,
            0,
            xb,
            ymid,
            xtop,
            b.y2,
            delta=sd,
        )
