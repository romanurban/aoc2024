import os
import inspect
import time

def get_day_number():
    """
    Extracts the day number from the caller script's filename.

    Returns:
    - int: The day number extracted from the filename.
    """
    # Traverse the call stack to find the first caller outside of aoc_utils.py
    for frame_info in inspect.stack():
        module = inspect.getmodule(frame_info.frame)
        if module is not None and hasattr(module, '__file__'):
            filename = module.__file__
            basename = os.path.basename(filename)
            if basename != 'aoc_utils.py':
                # Assuming the filename format is 'dayXX.py'
                day_str = ''.join(filter(str.isdigit, basename))
                if not day_str:
                    raise ValueError(f"No day number found in filename '{basename}'.")
                return int(day_str)
    raise ValueError("Cannot determine caller's filename.")

def get_input(day=None, filename=None, sample=False):
    """
    Reads input data for a given day or from a specified file.

    Parameters:
    - day (int): The day number. If None and filename is not provided, attempts to auto-detect.
    - filename (str): The input file to read from. Overrides day if provided.
    - sample (bool): Whether to read the sample input.

    Returns:
    - list: A list of input lines.
    """
    if filename:
        input_filename = filename
    else:
        if day is None:
            day = get_day_number()
        input_filename = f'inputs/day{int(day):02d}{"_sample" if sample else ""}.txt'

    try:
        with open(input_filename, 'r') as file:
            input_lines = [line.rstrip('\n') for line in file]
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file '{input_filename}' not found.")
    return input_lines

def timer(func):
    """
    Decorator to measure the execution time of a function, checking a global variable.
    """
    def wrapper(*args, **kwargs):
        if getattr(wrapper, 'enabled', True):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            elapsed = end_time - start_time
            print(f"{func.__name__} took {elapsed:.6f} seconds")
        else:
            result = func(*args, **kwargs)
        return result
    wrapper.enabled = True  # Default value
    return wrapper
