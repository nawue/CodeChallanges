def Solve2(H1,D,day):
    H1.pop(0)
    if H1 == []:
        return True
    
    for i in range(day,D+1):         
        if i%H1[0] == 0:
            return Solve2(H1[:],D,i)
            
    return False


def Solve(H, D):
    for day in range(D, 0, -1):     
        if (day%H[0] == 0) and Solve2(H[:],D,day):                    
            return day

def main():
    cases = int(input())
    for case in range(cases):
        N, D = [int(_) for _ in input().split()]      
        H = [int(_) for _ in input().split()]
        print("Case #{}: {}".format(case + 1, Solve(H, D)))     

if __name__ == '__main__':
    main()