from PyQt5.QtCore import QDate


class DateFormater:
    @staticmethod
    def format_date_value(value):
        """Helper function to format QDate values to a string format."""
        if isinstance(value, QDate):
            return value.toString("dd.MM.yyyy")
        return value