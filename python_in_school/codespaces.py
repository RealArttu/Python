import random


for j in range(0,5,1):
    luvut = []
    for i in range(0, random.randint(2,5)*2,1):
        luvut.append(random.randint(0,10))
    print("Luvut:", luvut)
    
    print("Koko listan alkioiden summa:", summa)
    print("Listan ensimmaisten", int(len(luvut)/2), " alkion summa:", puolisumma)
    print()