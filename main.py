def sort(tab : list) -> list[int]:
    dico: dict[int, int] = {}
    for i in tab:
        dico[i] = dico.get(i, 0) + 1
    tab = []
    for i in range(min(tab), max(tab)+1, step):
        for _ in range(dico.get(i, 0)):
            tab.append(i)
    return tab
