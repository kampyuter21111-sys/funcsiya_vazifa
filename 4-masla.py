def umumiy_sonlar(a, b):
    natija = []
    for son in a:
        if son in b and son not in natija:
            natija.append(son)
    return natija


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(umumiy_sonlar(a, b))