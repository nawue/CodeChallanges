
def Solve(N,K,V):

    if V == []:
        return 0

    match=1
    V.sort()
    V.sort(key=len, reverse=False)
    
    for i in range(1, len(V)):
        if V[0] == V[i]:
            match += 1
    
    if match >= K:
        match = len(V[0])
    if match == 1 and len(V[0]) != 1:
        match = 0

    auxV = [k for k in V if len(k) > len(V[0])]
    
    return match + Solve(N,K,auxV)


def main():
    cases = int(input())
    
    for case in range(cases):
        N, K = [int(_) for _ in input().split()]
        V=[]
        for i in range(N):
            V.append(input())
        print("Case #{}: {}".format(case + 1, Solve(N, K, V)))       

if __name__ == '__main__':
    main()
