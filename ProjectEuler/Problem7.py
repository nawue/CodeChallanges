solve = False
num = 14
i = 6
primes = [2,3,5,7,11,13]

while not solve:
    aux = False
    for prim in primes:
        if num % prim == 0:
            aux = True
    if aux == False:
        i+=1
        primes.append(num)
    
    if i == 10001: solve = True
    num +=1 

print(num-1)
