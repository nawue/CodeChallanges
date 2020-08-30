def Solve(B, A):
    res = 0
    s = 0
    A.sort()
    for i in A:
        s += i
        if s > B:
            return res
        else:
            res += 1
    return res

def main():
    cases = int(input())
    for case in range(cases):
        N, B = [int(_) for _ in input().split()]      
        A = [int(_) for _ in input().split()]
        if N == 0 or B == 0:
            print("Case #{}: {}".format(case + 1, 0))  
        else:
            print("Case #{}: {}".format(case + 1, Solve(B, A)))       

if __name__ == '__main__':
    main()
