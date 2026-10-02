import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs import Glyph
from draw.arch import draw_arch
from draw.corner import draw_corner
from draw.rect import draw_rect


class LowercaseAGlyph(Glyph):
    name = "lowercase_a"
    unicode = "0x61"
    accent_x_offset = 16
    mid_height = 0.53
    width_ratio = 0.883760
    taper = 0.55
    sbl = 0.569643
    sbr = 0.906786
    bold_width_ratio = 0.990909
    bold_sbl = 0.581281
    bold_sbr = 0.927203

    stroke_x_ratio = 0.98
    stroke_alt_ratio = 0.97
    bot_hx_ratio = 0.95
    bot_hy_ratio = 0.65
    mid_hx_ratio = 1.4
    mid_hy_ratio = 0.9
    right_cap_hx_ratio = 1.05
    right_cap_hy_ratio = 0.63
    cap_mid_offset = 0.031
    cap_hx_ratio = 1.05
    cap_hy_ratio = 1.4
    cap_x_stroke_ratio = 1.1
    cap_y_stroke_ratio = 0.98
    cap_start_height = 0.68
    cap_height = 0.74
    cap_offset = 0.02
    thinning = 0.9
    upper_bowl_mid = 0.54
    ending_thickness = 0.7
    overshoot_top = True
    overshoot_bottom = True

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        ec = self.extra_cut(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y
        sa = dc.stroke_alt * self.stroke_alt_ratio
        csx, csy = (
            dc.stroke_x * self.cap_x_stroke_ratio,
            dc.stroke_y * self.cap_y_stroke_ratio,
        )
        ymid = b.y1 + self.mid_height * b.height
        xmc = b.xmid + self.cap_mid_offset * b.width
        ycap = b.y1 + self.cap_start_height * b.height
        yl = ymid + sa / 2
        hx, hy = b.hx * self.bot_hx_ratio, b.hy * self.bot_hy_ratio
        bhx, bhy = self.mid_hx_ratio * b.hx, self.mid_hy_ratio * b.hy
        ycut = b.y1 + self.cap_height * b.height
        xc = b.x1 + self.cap_offset * b.width
        chx, chy = self.cap_hx_ratio * b.hx, self.cap_hy_ratio * b.hy
        rchx = self.right_cap_hx_ratio * b.hx
        rchy = self.right_cap_hy_ratio * b.hy

        # Lower half half of the bowl
        draw_arch(
            pen,
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            yl,
            hx,
            hy,
            taper=self.taper * dc.taper,
            side="right",
            cut="top",
        )

        # Upper half of the bowl
        draw_corner(
            pen,
            sx,
            sa,
            b.x1,
            (b.y1 + yl) / 2,
            b.x2 - sx,
            yl,
            bhx,
            bhy,
            orientation="top-right",
        )

        # Cap
        draw_corner(
            pen, sx, csy, b.x2, ycap, xmc, b.y2, rchx, rchy, orientation="top-left"
        )

        loop_glyph = ufoLib2.objects.Glyph()
        draw_corner(
            loop_glyph.getPen(),
            csx * self.thinning,
            csy,
            xc,
            b.ymid,
            xmc,
            b.y2,
            chx,
            chy,
            orientation="top-right",
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(cut_glyph.getPen(), b.x1, b.ymid, b.xmid, ycut - ec)
        result = BooleanGlyph(loop_glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)

        # Stem
        draw_rect(
            pen,
            b.x2 - sx,
            0,
            b.x2,
            ycap,
        )
