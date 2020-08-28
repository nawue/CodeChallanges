#4436271

#Si resto, busco el primer impar por la izquierda. Le resto uno y pongo todo a la derecha
# a 8

#4428888

# y los resto
#52,617


# Si sumo, busco el primer impar le sumo uno al de la izquierda y pongo 0
#En caso de quedar impar le sumo otro
#4500000 -> 4600000

#y resto
#163,729

# Si todos los numeros son impares devuelve true
def oddPos(number):
    for idx, v in enumerate(number):
        if number[idx] % 2 != 0:
            return idx
    return -1
    
def concatenate(list):
    result= ''
    for element in list:
        result += str(element)
    return result


import math
def f(x, y):
    a = math.floor(math.log10(y))
    return int(x*10**(1+a)+y)

N = 6488962
def restar(N):
    aux = [int(i) for i in str(N)]
    pos = oddPos(aux)
    aux[pos] = aux[pos] - 1
    if aux[0] == 0:
        aux.remove(aux[0])
    for i in range(pos+1, len(aux)):
        aux[i] = 8
    return int(concatenate(aux))

def sumar(N):
    aux = [int(i) for i in str(N)]
    pos = oddPos(aux)
    if aux[pos] == 9 and pos != 0:
        aux[pos] = 0
        aux[pos-1] = aux[pos-1] + 1
        aux = sumar(int(concatenate(aux)))
        aux = [int(i) for i in str(aux)]
    elif aux[pos] == 9 and pos == 0:
        aux[pos] = 0
        aux.insert(0, 2)
    else:
        aux[pos] = aux[pos] + 1
    for i in range(pos+1, len(aux)):
            aux[i] = 0
    return int(concatenate(aux))

number1 = N - restar(N)
number2 = sumar(N) - N
print('Case1 #{}: {}'.format(1, number1))
print('Case1 #{}: {}'.format(1, number2))
