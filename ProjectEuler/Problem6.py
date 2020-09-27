
import math

aux = 0
aux2 = 0
for i in range(1,11):
    aux += i
    aux2 += pow(i,2)

print(aux2 - pow(aux,2))

