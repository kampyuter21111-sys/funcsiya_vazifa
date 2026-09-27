def oxirgi_nollar(sonlar):
    nollar = 0
    for i in range(27):
        if sonlar[i] != 0:
            sonlar[nollar], sonlar[i] = sonlar[i], sonlar[nollar]
            nollar += 1
    return sonlar


son = [3,4,0,0,0,6,2,0,6,7,6,0,0,0,9,10,7,4,4,5,3,0,0,2,9,7,1]
print(oxirgi_nollar(son))