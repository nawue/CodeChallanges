
def Solve(N,X,A):
    res = [0 for _ in A]
    res2 = [0 for _ in A]
    out = 1
    fin = sum([_ for _ in range(1,N+1)])

    while sum(res) != fin:
        for i in range(N):
            A[i] -= X
            if A[i] <= 0 and res2[i] == 0:
                res2[i] = out
                out += 1
            res[res2[i]-1] = i+1

    return res

def main():
    cases = int(input())
    for case in range(cases):
        N, X = [int(_) for _ in input().split()]      
        A = [int(_) for _ in input().split()]
        print("Case #{}: ".format(case + 1),end='') 
        aux = Solve(N,X,A)
        print(*aux, sep=' ' )

if __name__ == '__main__':
    main()



