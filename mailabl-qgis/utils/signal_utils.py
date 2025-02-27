from contextlib import contextmanager
from PyQt5.QtWidgets import QPushButton

@contextmanager
def block_signals(widget):
    """
    Context manager to temporarily block signals for a widget.

    This is useful when you want to suppress signal emissions temporarily,
    such as when making multiple changes to a widget's state without triggering its connected slots.

    Why use a context manager?
    --------------------------
    1. Simplifies Resource Management:
       - Automatically blocks signals when entering the 'with' block and unblocks them when exiting.

    2. Ensures Proper Cleanup:
       - Guarantees signals are unblocked even if an error occurs inside the block.

    3. Enhances Code Readability:
       - The 'with' statement makes it clear where signals are suppressed.

    Example usage:
        with block_signals(my_button):
            my_button.setChecked(True)
            my_button.setText("Updated")

    Without context manager:
        my_button.blockSignals(True)
        try:
            my_button.setChecked(True)
            my_button.setText("Updated")
        finally:
            my_button.blockSignals(False)
    """
    widget.blockSignals(True)
    try:
        yield
    finally:
        widget.blockSignals(False)


def execute_with_block(button: QPushButton, func, *args, **kwargs):
    """
    Function to temporarily disable a button while executing a task.

    This prevents multiple clicks or accidental re-triggering of the button's action
    until the task is completed. Once the function finishes, the button is re-enabled.

    Why not use a context manager here?
    ----------------------------------
    1. Direct Interaction Control:
       - 'setEnabled(False)' directly disables user interaction, which is straightforward.

    2. Simple Functionality:
       - Disabling/re-enabling buttons is simple and doesn’t require the added structure of a 'with' statement.

    3. Flexibility:
       - Easier to call directly inside lambda functions or callbacks without wrapping in a context manager.

    Args:
        button (QPushButton): The button to be temporarily disabled.
        func (callable): The function to execute while the button is disabled.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.

    Example usage:
        execute_with_block(my_button, some_function, arg1, arg2, key=value)
    """
    if button:
        button.setEnabled(False)  # Disable the clicked button
        try:
            func(*args, **kwargs)  # Execute the connected function
        finally:
            button.setEnabled(True)  # Re-enable the button after function execution


def reset_buttons(self, active_button, button_names):
    """
    Resets the state of multiple buttons, re-enabling them after a process is complete.

    Args:
        self: Reference to the main UI class.
        active_button (QPushButton): The button that triggered the process.
        button_names (list): List of button attribute names to re-enable.

    Example usage:
        reset_buttons(self, clicked_button, ['pbContracts_Connect_properties', 'pbProjects_Connect_properties'])
    """
    buttons = [getattr(self, name, None) for name in button_names]
    for button in buttons:
        if button:
            button.setEnabled(True)
    if active_button:
        active_button.setEnabled(True)
    self.showNormal()


def disable_buttons(self, button_names, active_button=None):
    """
    Disables a list of buttons, preventing user interaction during a process.

    Args:
        self: Reference to the main UI class.
        button_names (list): List of button attribute names to disable.
        active_button (QPushButton, optional): The button that triggered the process (if applicable).

    Example usage:
        disable_buttons(self, ['pbContracts_Connect_properties', 'pbProjects_Connect_properties'])
    """
    buttons = [getattr(self, name, None) for name in button_names]
    for button in buttons:
        if button:
            button.setEnabled(False)
    if active_button:
        active_button.setEnabled(False)
