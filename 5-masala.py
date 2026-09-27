N = int(input("N kiriting: "))
sonlar = list(map(int, input("Sonlarni kiriting: ").split()))

natija = [son for son in sonlar if sonlar.count(son) > 1]
print("sonlar =", natija)