import random

def expectedValue(n,k,v):
    aux = 0
    E = []
    E.append(sum(v)/n)

    if k==0:
        return E[0]

    for i in range(1,k+1):
        if random.choice(v) >= E[-1] or k==1:
            for j in v:
                aux += max(j, E[-1])
            return aux/n
        else:
            for j in v:
                aux += max(j, E[-1])
            E.append(aux/n)
            aux=0
            if i == k:
                return E[-1]

def main():
    cases = int(input())
    for case in range(cases):
        n, k = [int(_) for _ in input().split()]
        v = [int(_) for _ in input().split()]
        print("Case #{}: {}".format(case + 1, expectedValue(n,k,v)))       

if __name__ == '__main__':
    main()
