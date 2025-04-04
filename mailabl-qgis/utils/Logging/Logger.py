import os
import traceback
import datetime
import logging
from typing import Optional

class TracebackLogger:
    @staticmethod
    def log_traceback(custom_message: Optional[str] = None,
                      use_logging: bool = False,
                      stack_limit: Optional[int] = None,
                      log_to_file: bool = False,
                      log_dir: str = "Logs") -> str:
        """
        Generate and log a formatted traceback of the current call stack with additional context.
        Optionally, if log_to_file is True, the traceback is saved to a uniquely named log file in the specified logs directory.

        :param custom_message: Optional[str]
            A custom message to include with the traceback.
        :param use_logging: bool
            If True, logs the traceback using Python's logging module at the DEBUG level.
        :param stack_limit: Optional[int]
            Limit the number of stack frames to include in the traceback.
        :param log_to_file: bool
            If True, writes the traceback to a new log file in the specified logs directory.
        :param log_dir: str
            Directory where log files are saved (default is 'logs').
        :return: str
            A formatted string representing the call stack with additional context.
        """
        # Get the current timestamp.
        timestamp = datetime.datetime.now().isoformat()
        
        # Generate the traceback string with an optional stack frame limit.
        if stack_limit is not None:
            stack = traceback.format_list(traceback.extract_stack(limit=stack_limit))
            tb_str = "".join(stack)
        else:
            tb_str = "".join(traceback.format_stack())
        
        # Build the output with a timestamp and optional custom message.
        output = f"[{timestamp}]"
        if custom_message:
            output += f" {custom_message}\n"
        output += tb_str

        # Print the traceback output.
        print(output)

        # Optionally log the output using the logging module.
        if use_logging:
            logging.debug(output)
        
        # Optionally write the output to a file.
        if log_to_file:
            # Ensure the log directory exists.
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)
            # Create a unique file name for the log file using a timestamp.
            file_timestamp = datetime.datetime.now().isoformat(timespec='seconds').replace(":", "-")
            file_name = f"error_log_{file_timestamp}.log"
            file_path = os.path.join(log_dir, file_name)
            try:
                with open(file_path, "w") as file:
                    file.write(output)
            except Exception as e:
                print(f"Failed to write error log to file {file_path}: {e}")
            print(f"Error log created: {file_path}")

        return output
