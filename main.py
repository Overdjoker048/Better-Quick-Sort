import math
from typing import Union

def sort(tab: list) -> list[Union[float, int]]:
    # If the input list is empty, return an empty list
    if not tab:
        return []
    
    # Initialize variables
    deci: Union[None, int] = None  # Variable to determine the scaling factor for sorting
    count: dict[float, int] = {}  # Dictionary to count occurrences of each number

    # Iterate through the input list to populate the count dictionary and determine the scaling factor
    for i in tab:
        count[i] = count.get(i, 0) + 1  # Increment the count for the current number
        ldeci = math.floor(math.log10(abs(i))) - 2  # Calculate the logarithmic scale of the number
        if deci is None or ldeci < deci:  # Update the scaling factor if necessary
            deci = ldeci
    
    # Calculate the scaling factor to normalize the numbers
    deci = 10 ** (-1 * deci)
    result = []  # Initialize the result list

    # Iterate through the range of scaled numbers to reconstruct the sorted list
    for i in range(math.floor(min(tab)) * deci, math.ceil(max(tab)) * deci + 1):
        i = i / deci  # Scale the number back to its original value
        c = count.get(i, 0)  # Get the count of the current number
        if c != 0:  # If the number exists in the input list
            result.extend([i] * c)  # Add it to the result list the appropriate number of times
    
    # Return the sorted list
    return result
