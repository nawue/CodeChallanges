def Solve(H, D):
    for h in H[::-1]:     
        D = (D // h) * h #Smallest multiple of Hi greater than or equal to D
    return D

def main():
    cases = int(input())
    for case in range(cases):
        N, D = [int(_) for _ in input().split()]      
        H = [int(_) for _ in input().split()]
        print("Case #{}: {}".format(case + 1, Solve(H, D)))     

if __name__ == '__main__':
    main()