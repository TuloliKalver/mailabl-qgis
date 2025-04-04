class SelectionConfirmation:
    @staticmethod
    def confirm_county_selection():
        """Confirms county selection and clears next stage selections."""
        from .SelectionActions import SelectionActions  # Lazy import to avoid circular import
        SelectionActions.show_message("Confirmation", "Confirming county selection...")

    @staticmethod
    def confirm_municipality_selection():
        """Confirms municipality selection and clears settlement selection."""
        from .SelectionActions import SelectionActions  # Lazy import
        SelectionActions.show_message("Confirmation", "Confirming municipality selection...")

    @staticmethod
    def confirm_settlement_selection():
        """Confirms settlement selection and updates displayed selections."""
        from .SelectionActions import SelectionActions  # Lazy import
        SelectionActions.show_message("Confirmation", "Confirming settlement selection...")
