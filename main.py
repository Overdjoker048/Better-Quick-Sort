def sort(tab: list) -> list[int]:
    # Create a dictionary to count occurrences of each number
    dico: dict[int, int] = {}
    for i in tab:
        dico[i] = dico.get(i, 0) + 1
    
    # Initialize an empty list to store the sorted numbers
    tab = []
    
    # Iterate over the range from the minimum to the maximum value in the input list
    for i in range(min(tab), max(tab) + 1):
        # Append each number to the sorted list according to its frequency
        for _ in range(dico.get(i, 0)):
            tab.append(i)
    
    # Return the sorted list
    return tab
