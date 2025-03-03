# Adaptive Sorting Program

## Description
This program implements a variant of counting sort specifically adapted to handle integer  numbers.

## Operation

### Parameters
- **Input**: List of numbers (integers)
- **Output**: Sorted list of numbers

### Sorting Process
1. **Analysis Phase**
   - Determination of minimum and maximum values
   - Automatic calculation of optimal step for decimal numbers
   - Counting occurrences of each number

2. **Reconstruction Phase**
   - Creation of a new sorted array
   - Insertion of numbers respecting their frequency of occurrence

### Characteristics
- Intelligent handling of decimal numbers
- Preservation of duplicates
- Memory optimization through a counting dictionary

## Complexity
- **Time**: O(n + r)
  - n: array size
  - r: range of values ((max - min)/step)
- **Space**: O(k)
  - k: number of unique values

## Usage
```python
from main import sort

# Usage example
numbers = [3.14, 1.59, 2.65, 3.14, 1.0]
result = sort(numbers)
print(result)  # Displays the sorted list
```

## Key Features
- Efficient for limited number distributions
- Adapted for both decimal and integer numbers
- Maintains sorting stability
- Memory optimization through counting dictionary
