def Solve(H):
    res = 0
    for i in range(1, len(H)):
        if (i+1) < len(H):
            if (H[i-1] < H[i] and H[i+1] < H[i] ):
                res+=1
                i+=1
    return res



def main():
    cases = int(input())
    for case in range(cases):
        N = [int(_) for _ in input().split()]
        H = [int(_) for _ in input().split()]
        print("Case #{}: {}".format(case + 1, Solve(H)))

if __name__ == '__main__':
    main()
