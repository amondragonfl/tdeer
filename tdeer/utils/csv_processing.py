import os
import csv
from contextlib import contextmanager
import numpy as np 

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

def validate_csv(file_path):
    """
    Validate a CSV file by checking:
    - File exists
    - File extension is .csv
    - File has columns 'weight' and 'calories'

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        bool: True if the file is valid, False otherwise.
    """
    if not file_exists(file_path):
        print(f"File '{file_path}' does not exist.")
        return False
    
    if not file_path.lower().endswith('.csv'):
        print(f"File '{file_path}' is not a CSV file.")
        return False
    
    try:
        with open_csv(file_path, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Read the header
            if 'weight' not in header or 'calories' not in header:
                print(f"File '{file_path}' does not have 'weight' and 'calories' columns.")
                return False
            # Check if data follows the structure (weight, calories)
            for row in reader:
                if len(row) < 2:
                    print(f"File '{file_path}' has rows with missing data.")
                    return False
                try:
                    weight_index = header.index('weight')
                    calories_index = header.index('calories')
                    float(row[weight_index])  
                    float(row[calories_index]) 
                except ValueError:
                    print(f"File '{file_path}' has invalid data (non-numeric values) in the 'weight' or 'calories' columns.")
                    return False
                except IndexError:
                    print(f"File '{file_path}' is missing data in either the 'weight' or 'calories' column.")
                    return False
            
    except Exception as e:
        print(f"Error processing the file: {e}")
        return False
    # If all checks pass
    return True

def read_csv_as_numpy(file_path):
    """
    Reads a CSV file and returns two numpy arrays representing the data.

    This function assumes that the CSV file contains two columns where:
    - The first column is assigned to weight.
    - The second column is assigned to calories.
    
    The first row of the CSV is skipped as it is assumed to be a header.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        tuple: A tuple containing two numpy arrays:
            - X: A numpy array representing the data from the first column.
            - Y: A numpy array representing the data from the second column.
    """
    data = np.genfromtxt(file_path, delimiter=',', skip_header=1)
    weight = data[:, 0]  
    calories = data[:, 1] 
    return weight, calories

