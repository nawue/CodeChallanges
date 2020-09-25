
def Solve(N, V1, H1, A, B, C, D, E, F, M):
    res = 0
    V=[]
    H=[]
    V.append(V1)
    H.append(H1)
    for i in range(1, N):
        V.append( ( A*V[i-1] + B*H[i-1] + C ) % M)
        H.append( ( D*V[i-1] + E*H[i-1] + F ) % M)

    firscoord = [V1, H1]
    for i in range(0, 1000-V1):
        if V1 == V[i]:
            secondcoord = [V[i], H[i]]


    return res


#  N, V1, H1, A, B, C, D, E, F and M. 

def main():
    cases = int(input())
    for case in range(cases):
        N, V1, H1, A, B, C, D, E, F, M = [int(_) for _ in input().split()]      
        print("Case #{}: {}".format(case + 1, Solve(N, V1, H1, A, B, C, D, E, F, M)))       

if __name__ == '__main__':
    main()

