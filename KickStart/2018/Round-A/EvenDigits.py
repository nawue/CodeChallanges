import math

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

def f(x, y):
    a = math.floor(math.log10(y))
    return int(x*10**(1+a)+y)

def restar(N):
    aux = [int(i) for i in str(N)]
    pos = oddPos(aux)
    if pos == -1:
        return N    
    aux[pos] = aux[pos] - 1
    if aux[0] == 0:
        aux.remove(aux[0])
        if aux == []:
            return 1
        for idx, v in enumerate(aux):
            aux[idx]=8
    else:
        for i in range(pos+1, len(aux)):
            aux[i] = 8

    return int(concatenate(aux))

def sumar(N):
    aux = [int(i) for i in str(N)]
    pos = oddPos(aux)
    if pos == -1:
        return N
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


def main():
    cases = int(input())
    for case in range(cases):
       N = int(input())
       if N == 1:
           print("Case #{}: {}".format(case + 1, 1))
       else:
           number1 = N - restar(N)
           number2 = sumar(N) - N
           if (number1 <= number2):
                   print("Case #{}: {}".format(case + 1, number1))
           else:
                   print("Case #{}: {}".format(case + 1, number2))
        

if __name__ == '__main__':
    main()