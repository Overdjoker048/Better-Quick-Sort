import math

def better_quick_sort(tab: list) -> list[int]:
    if not tab:
        return []
    
    deci = None
    count: dict[float, int] = {}

    for i in tab:
        count[i] = count.get(i, 0) + 1
        decil = math.floor(math.log10(abs(i))) - 2
        if deci is None or decil < deci:
            deci = decil
    multi = 10 ** (-1*deci)
    result = []
    for i in range(math.floor(min(tab))*multi, math.ceil(max(tab))*multi + 1):
        i = i/multi
        c = count.get(i, 0)
        if c != 0:
            result.extend([i] * c)
    return result