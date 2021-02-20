import random



dizi = []
for x in range(1,100):
    for asal in range(2,x):
        if (x % asal) == 0:
            break
        elif(x % asal !=0) and (asal == x-1):
            dizi.append(x)


numaralar=(random.sample(dizi,3),
           random.sample(dizi,3),
           random.sample(dizi,3))
for i in numaralar:
    print(i)

