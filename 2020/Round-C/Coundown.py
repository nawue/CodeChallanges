def Solve(N,A,K):
    #A.reverse()
    res=0
    auxK = K
    for i in range(N):
        if A[i] == auxK:
            auxK-=1
            if auxK == 0:
                res  += 1
                auxK = K
        elif A[i] == K and K!=auxK:
            auxK = K -1
        else:
            auxK = K

        print("auxK = {}; A[i] = {}; res = {}".format(auxK, A[i], res))

    return res


def main():
    cases = int(input())
    for case in range(cases):
        N, K = [int(_) for _ in input().split()]
        A = [int(_) for _ in input().split()]
        print("Case #{}: {}".format(case + 1, Solve(N,A,K)))

if __name__ == '__main__':
    main()
