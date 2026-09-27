def listlarni_birlashtir(list1, list2):
    natija = []
    uzunlik = max(len(list1), len(list2))
    
    for i in range(uzunlik):
        if i < len(list1):
            natija.append(list1[i])
        if i < len(list2):
            natija.append(list2[i])
    
    return natija


list1 = [1, 2, 3]
list2 = [11, 22, 33]
print(listlarni_birlashtir(list1, list2))