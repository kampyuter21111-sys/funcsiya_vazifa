def belgilar_soni(a):
    natija = {}
    for i in a:
        if i in natija:
            natija[i] += 1
        else:
            natija[i] = 1
    return natija


print(belgilar_soni('w3resource'))