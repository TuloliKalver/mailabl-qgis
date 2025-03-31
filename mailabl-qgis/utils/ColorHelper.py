from colorsys import hls_to_rgb, rgb_to_hls
from PyQt5.QtGui import QColor, QRadialGradient

class ColorUtils:


    @staticmethod
    def _get_text_color_for_background(rgb):
        """
        Determines a text color (light or dark variant) that contrasts well with the background,
        but avoids overly harsh black/white extremes.
        """
        r, g, b = rgb
        brightness = (r * 299 + g * 587 + b * 114) / 1000

        if brightness < 128:
            # Background is dark → return soft light text
            return QColor(240, 240, 255)
        else:
            # Background is light → return soft dark text
            return QColor(40, 40, 50)

    @staticmethod
    def hex_to_rgb(hex_code):
        #print(f'hex code is {hex_code}')
        clean_hex_code = hex_code.strip('#')
        return tuple(int(clean_hex_code[i:i+2], 16) for i in (0, 2, 4))

    @staticmethod
    def rgb_to_hex(rgb_tuple):
        return "#{:02x}{:02x}{:02x}".format(*rgb_tuple)

    @staticmethod
    def soften_edge(rgb, darkness=0.8, saturation_drop=0.95):
        r, g, b = [x / 255.0 for x in rgb]
        h, l, s = rgb_to_hls(r, g, b)
        l *= darkness
        s *= saturation_drop
        r, g, b = hls_to_rgb(h, min(l, 1.0), min(s, 1.0))
        return tuple(int(x * 255) for x in (r, g, b))

    
    @staticmethod
    def radial_gradient_for_painter(hex_color, rect):
        main_rgb = ColorUtils.hex_to_rgb(hex_color)
        halo_rgb = ColorUtils.soften_edge(main_rgb)
        
        #frame_rgb = ColorUtils.soften_edge(main_rgb)
        
        
        #radius = max(rect.width(), rect.height()) * 0.6
        #gradient = QRadialGradient(rect.center().x(), rect.center().y() + 4, radius)

        #gradient = QRadialGradient(rect.center(), rect.width() * 0.6)

        #radius = 10  # 10 pixels radius glow
        #gradient = QRadialGradient(rect.center().x(), rect.center().y() + 10, radius)


        gradient = QRadialGradient(rect.center().x(), rect.center().y() + 2, rect.width() * 0.6)
        gradient.setColorAt(0, QColor(*main_rgb))
        gradient.setColorAt(1, QColor(*halo_rgb))


        gradient.setColorAt(0, QColor(*main_rgb))
        gradient.setColorAt(1, QColor(*frame_rgb))

        return gradient