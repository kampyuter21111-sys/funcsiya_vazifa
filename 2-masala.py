def dublikat(royxat):
    natija = []
    korilgan = []
    
    for i in royxat:
        if i not in korilgan:
            natija.append(i)
            korilgan.append(i)
    
    return natija


son = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print(dublikat(son))