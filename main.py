def better_quick_sort(tab: list) -> list[int]:
    #Return an empty list if tab is empty
    if not tab:
        return []

    # Create a dictionary to count occurrences of each number
    count: dict[int, int] = {}
    
    for i in tab:
        count[i] = count.get(i, 0) + 1

    # Initialize an empty list to store the sorted numbers
    result = []
    
    #Iterate over the range from the minimum to the maximum value in the input list
    for i in range(min(tab), max(tab) + 1):
        #Append each number to the sorted list according to its frequency
        c = count.get(i, 0)
        if c != 0:
            result.extend([i] * c)

    #Return the sorted list
    return result
