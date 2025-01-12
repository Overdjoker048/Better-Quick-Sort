def sort(tab : list) -> list[int]:
    dico: dict[int, int] = {}
    maxv: int = tab[0]
    minv: int = tab[0]
    step = 1
    for i in tab:
        if i > maxv:
            maxv = i
        elif i < minv:
            minv = i
        istep = 10 ** -(len(str(i).split('.')[1]))
        if istep < step:
            step = istep
        if dico.get(i):
            dico[i] += 1
        else:
            dico[i] = 1
    tab = []
    for i in range(minv, maxv+1, step):
        for _ in range(dico.get(i, 0)):
            tab.append(i)
    return tab
