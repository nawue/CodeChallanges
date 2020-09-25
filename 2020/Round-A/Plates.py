def Solve(N, K, P, V, sumV):
    dp = []
    dp.append([0] * (P + 1))
    for j in range(min(K, P) + 1):
        dp[0][j] = sumV[0][j]

    for i in range(1, N):
        dp.append([0]*(P+1))
        for j in range(P+1):
            dp[i][j] = dp[i-1][j]
            for x in range(min(j,K)+1):                   
                if dp[i][j] < dp[i - 1][j - x] + sumV[i][x]:
                     dp[i][j] = dp[i - 1][j - x] + sumV[i][x]

    return dp[N-1][P]
    

def main():
    cases = int(input())
    
    for case in range(cases):
        N, K, P = [int(_) for _ in input().split()]
        V=[]
        sumV=[]
        for i in range(0,N):
            auxV = [int(_) for _ in input().split()]
            V.append(auxV)
            v = [0]
            for j in range(K):
                v.append(v[-1] + V[i][j])
            sumV.append(v)

        print("Case #{}: {}".format(case + 1, Solve(N, K, P, V, sumV)))       

if __name__ == '__main__':
    main()
