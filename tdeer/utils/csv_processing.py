import os
import csv
from contextlib import contextmanager

@contextmanager
def open_csv(file_path, mode='r', newline=''):
     
    """
    Context manager to open a CSV file safely.

    Args:
        file_path (str): The path to the CSV file.
        mode (str): The mode to open the file in ('r' for reading, 'w' for writing, etc.).
        newline (str): The newline character to use in writing. Default is ''.

    Returns:
        file object: The opened CSV file object.
    """
     
    # Check if file exists
    if not file_exists(file_path):
        raise FileNotFoundError((f"The file at '{file_path}' does not exist."))
    
    try:
        file = open(file_path, mode, newline=newline)
        yield file
    except Exception as e:
        print(f"Error opening or processing the file: {e}")
        raise 
    finally:
        file.close()


def file_exists(file_path):
    """
    Check if a file exists at the specified path.

    Args:
        file_path (str): The path to the file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.isfile(file_path)

