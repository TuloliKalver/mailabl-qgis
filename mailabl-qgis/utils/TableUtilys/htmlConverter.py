# file: utils/TableUtilys/htmlConverter.py

import re

class HtmlConverter:
    """
    Convert arbitrary HTML+inline-CSS into a subset that QTextBrowser (QGIS hover popup)
    can render—with only supported properties and legacy table bgcolor/width attrs.
    """

    # CSS props QTextBrowser supports as inline style
    _SUPPORTED_PROPS = {
        'background-color', 'color', 'font-size', 'font-family',
        'padding', 'margin', 'border', 'text-align'
    }

    @classmethod
    def convert(cls, raw_html: str) -> str:
        html = raw_html

        # 1. Drop any <style>…</style> blocks outright
        html = re.sub(r'<style.*?>.*?</style>', '', html, flags=re.DOTALL | re.IGNORECASE)

        # 2. Convert <table … style="…"> → <table bgcolor="…" width="…" …>
        def _table_repl(m):
            pre_attrs = m.group(1) or ''
            style = m.group(2) or ''
            post_attrs = m.group(3) or ''

            # parse declarations, normalize 'background' to 'background-color'
            decls = {}
            for part in style.split(';'):
                if ':' in part:
                    k, v = part.split(':', 1)
                    prop = k.strip().lower()
                    val = v.strip()
                    if prop == 'background':
                        prop = 'background-color'
                    decls[prop] = val

            attrs = pre_attrs
            # legacy bgcolor
            if 'background-color' in decls:
                attrs += f' bgcolor="{decls["background-color"]}"'
            # legacy width
            if 'width' in decls:
                attrs += f' width="{decls["width"]}"'

            return f'<table{attrs}{post_attrs}>'

        html = re.sub(
            r'<table([^>]*)\sstyle="([^"]*?)"([^>]*)>',
            _table_repl,
            html,
            flags=re.IGNORECASE
        )

        # 3. Filter ALL other style="…" attributes, keeping only supported props
        def _style_repl(m):
            style = m.group(1) or ''
            kept = []
            for part in style.split(';'):
                if ':' not in part:
                    continue
                prop, val = part.split(':', 1)
                prop_l = prop.strip().lower()
                val_s = val.strip()
                # normalize 'background' shorthand
                if prop_l == 'background':
                    prop_l = 'background-color'
                if prop_l in cls._SUPPORTED_PROPS:
                    kept.append(f'{prop_l}: {val_s}')
            if kept:
                # join declarations with semicolon
                decls = "; ".join(kept)
                return f'style="{decls}"'
            return ''

        html = re.sub(r'style="([^"]*?)"', _style_repl, html, flags=re.IGNORECASE)

        return html
