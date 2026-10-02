from draw.loop import draw_loop
from draw.corner import draw_corner
from draw.rect import draw_rect
import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs.lowercase.round import RoundLowercaseGlyph


class LowercaseEGlyph(RoundLowercaseGlyph):
    name = "lowercase_e"
    unicode = "0x65"
    mid_height = 0.52
    thinning = 0.9
    hx_ratio = 1
    tail_offset = 0.03
    tail_height = 0.27
    tail_hx_ratio = 1.15
    tail_hy_ratio = 1.15
    width_ratio = 0.961219
    bold_width_ratio = 1.047333
    sbl = 0.627738
    sbr = 0.634881
    bold_sbl = 0.614669
    bold_sbr = 0.673797

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        ec = self.extra_cut(dc)
        sx, sy = self.stroke_x_ratio * dc.stroke_x, self.stroke_y_ratio * dc.stroke_y
        yo = b.y1 + self.tail_height * b.height
        ymid = b.y1 + self.mid_height * b.height
        xt = b.x2 + self.tail_offset * b.width
        thx = self.tail_hx_ratio * b.hx
        thy = self.tail_hy_ratio * b.hy
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy

        # Half-left as the o-shape
        draw_loop(
            pen,
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            b.y2,
            hx,
            hy,
            cut="right",
        )
        # draw_corner(
        #     pen,
        #     sx,
        #     sy,
        #     b.x1,
        #     b.ymid,
        #     b.xmid,
        #     b.y2,
        #     hx,
        #     hy,
        #     orientation="top-right",
        # )

        # Top-right corner
        draw_corner(
            pen,
            sx * self.thinning,
            sy,
            b.x2,
            b.ymid,
            b.xmid,
            b.y2,
            hx,
            hy,
            orientation="top-left",
        )

        # bottom-left
        loop_glyph = ufoLib2.objects.Glyph()
        draw_corner(
            loop_glyph.getPen(),
            sx * self.thinning,
            sy,
            xt,
            b.ymid,
            b.xmid,
            b.y1,
            thx,
            thy,
            orientation="bottom-left",
        )

        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.xmid,
            yo + ec,
            b.xmid + b.width,
            b.ymid,
        )
        result = BooleanGlyph(loop_glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)

        draw_rect(
            pen,
            b.x1 + sx / 2,
            ymid,
            b.x2 - sx / 2,
            ymid + dc.stroke_alt / 2,
        )
        draw_rect(
            pen,
            b.x1 + sx / 2,
            ymid - dc.stroke_alt / 2,
            b.x2,
            max(ymid, b.ymid),
        )
