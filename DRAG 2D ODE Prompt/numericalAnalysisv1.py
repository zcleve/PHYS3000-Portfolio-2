# Zackary Cleveland PHYS3000
import numpy as np


def find_asymptotic_index(data , tolerance = 1e7 , n_consecutive = 10) :
    """
        Find the index of asymptotic behavior in a data array.

        Parameters:
        - data: NumPy array containing the data.
        - tolerance: Tolerance level for considering the behavior asymptotic (default is 1e7).
        - n_consecutive: Number of consecutive points required to satisfy the asymptotic condition (default is 10).

        Returns:
        - Index of asymptotic behavior.
    """
    output = 0.0  # Used as the check variable during the loop
    token = True  # Condition when checking for asymptotic behavior

    counter = 0  # Counter for successful occurrences of asymptotic behavior
    holder = np.zeros(n_consecutive)  # Placeholder for array that holds each row of the input data

    for i in range(data.size - 1) :
        if token :  # Initial step, and fall back step. Assigns initial check value
            output = data[i]
            counter = 0
            token = False
        elif counter < n_consecutive - 1 :  # Checks up to n_consecutive times for consecutive points within the tolerance of asymptotic behavior
            if np.abs(float(data[i + 1] - output)) <= tolerance :
                counter += 1
                output = data[i]
            else :
                token = True
        elif counter == n_consecutive - 1 :
            return i
    return "NO ASYMPTOTE"  # Will eventually learn exception handling for this
