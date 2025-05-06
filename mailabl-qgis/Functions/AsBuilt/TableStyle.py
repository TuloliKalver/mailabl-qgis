class TableStyle:
    # Global colors
    background_color = "#dfe3e1"
    text_color = "#243a4e"
    header_background = "#47a5b1"
    header_text_color = "white"
    shadow = "4px 4px 6px rgba(0, 0, 0, 0.15)"

    # Shared layout styles
    border_radius = "6px"
    transition = "all 0.3s ease-in-out"
    table_width = "90%"
    cell_padding = "2px 3px"
    header_padding = "2px 5px"
    font_size = "12px"
    font_family = "Roboto, Arial, sans-serif"

    @classmethod
    def shared_table_wrapper(cls, content: str, margin_top: str = "10px") -> str:
        return f"""
        <div style="display: flex; justify-content: center; margin-top: {margin_top};">
            <table style="
                border-collapse: collapse;
                width: {cls.table_width};
                background-color: {cls.background_color};
                border-radius: {cls.border_radius};
                box-shadow: {cls.shadow};
                transition: {cls.transition};
                text-align: left;
                font-family: {cls.font_family};
                color: {cls.text_color};
            ">
                {content}
            </table>
        </div>
        """

    @classmethod
    def build_header_cell(cls, label: str, width: str = "", emoji: str = "") -> str:
        return f"""
        <td style="font-weight: bold; font-size: {cls.font_size}; padding: {cls.header_padding}; width: {width}; color: {cls.header_text_color}; background: {cls.header_background};">
            <p><strong>{emoji} {label}</strong></p>
        </td>
        """
