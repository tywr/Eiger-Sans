from abc import ABC
from glyphs import Glyph


class SquareLowercaseGlyph(Glyph, ABC):
    """Define common class variables for all squared lowercase glyphs"""

    hx_ratio = 1.05
    hy_ratio = 0.75
    taper = 0.6
    width_ratio = 0.886
    ending_thickness = 0.8
    loop_ratio = 0.75

    sbr = 1
    sbl = 1
