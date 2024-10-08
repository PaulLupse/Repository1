#Ciurul lui Eratostene

Ciur = [0] * 1000005
Ciur[0] = Ciur[1] = 1
i = 2
while i <= 1000:
    if Ciur[i] == 0:
        j = 2
        while j <= 1000:
            Ciur[i*j] = 1
            j += 1
    i += 1
print(Ciur[:100])

