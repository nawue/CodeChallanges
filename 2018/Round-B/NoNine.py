def Solve(F, L):
    res = 0

    for N in range(F, L+1):
        if N%9 != 0 and str(N).find(str(9)) == -1:
            res+=1

    return res

def main():
    cases = int(input())
    for case in range(cases):
        F, L = [int(_) for _ in input().split()]      
        print("Case #{}: {}".format(case + 1, Solve(F, L)))       

if __name__ == '__main__':
    main()