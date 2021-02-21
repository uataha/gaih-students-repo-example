sayılar1 = range(2,1000)
def prime_first(param1):

    bolundu = False
    asal_sayı_liste = []
    for i in param1:
        bolundu = False
        for j in range(2,i):
            if i%j == 0:
                bolundu = True
        if bolundu == False:
            asal_sayı_liste.append(i)
    return asal_sayı_liste

print(prime_first(range(sayılar1[0],sayılar1[500])))

sayılar1 = range(2,1000)
def prime_second(param2):

    bolundu = False
    asal_sayı_liste = []
    for i in param2:
        bolundu = False
        for j in range(2,i):
            if i%j == 0:
                bolundu = True
        if bolundu == False:
            asal_sayı_liste.append(i)
    return asal_sayı_liste

print(prime_second(range(sayılar1[500],len(sayılar1))))


