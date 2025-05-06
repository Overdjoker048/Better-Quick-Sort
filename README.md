# Adaptive Sorting Program

## Description
This program implements a variant of counting sort specifically adapted to handle decimal numbers.

## Operation

### Parameters
- **Input**: List of numbers (decimals or integers)
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
- Intelligent handling of decimal and integer numbers (ℚ)
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
numbers = [314.15, 159.26, 265.35, 314.15, 10.01]
result = sort(numbers)
print(result)  # Displays the sorted list
```

## Key Features
- Efficient for limited number distributions
- Adapted for decimal and integer numbers (ℚ)
- Maintains sorting stability
- Memory optimization through counting dictionary
