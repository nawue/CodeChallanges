def Solve(N, K, M):
    diff1 = 0
    diffFinal = 0
    if K==1 and len(M)==1:
        return (M[0]+1) - M[0]
    for x in range(K):
        if len(M) == 1:
            M.insert(1, int(M[-1]+1))
        else:
            for i in range(1, len(M)):
                diff1 = (M[i] - M[i-1])
                if (diff1 > diffFinal and diff1 > 1):
                    diffFinal = diff1
                    pos = i-1
                if (i==len(M)-1 and diffFinal==0):
                    pos = len(M)-1
                    diffFinal=2
            M.insert(pos+1, int(M[pos]+diffFinal//2))
            diffFinal = 0

    for i in range(1, len(M)):
        diff1 = (M[i] - M[i-1])
        if diff1 > diffFinal:
            diffFinal = diff1
    
    return diffFinal

def main():
    cases = int(input())
    
    for case in range(cases):
        N, K = [int(_) for _ in input().split()]
        M = [int(_) for _ in input().split()]
        print("Case #{}: {}".format(case + 1, Solve(N, K, M)))       

if __name__ == '__main__':
    main()
