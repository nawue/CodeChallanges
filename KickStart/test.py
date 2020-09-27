cases = int(input())
for case in range(cases):
    A = []
    N, K = [int(_) for _ in input().split()]
    for i in range(N):
        A.append([int(_) for _ in input().split()])
    print("Case #{}: ".format(case + 1), end='')

    A.sort()
    robots = 1
    auxK = K
    auxA = [0 for _ in range(A[-1][1])]
    for a in A:
        for i in range(a[0], a[1]):
                auxA[i] = 1
    del A
    while auxA != []:
        if auxK > 0 and auxA[0] == 0 and auxK == K:
            del auxA[0]
        elif auxK > 0 and auxA[0] == 0 and auxK != K:
            del auxA[0]
            auxK -= 1
        elif auxA[0] == 1 and auxK > 0:
            auxK -= 1
            del auxA[0]
        elif auxK == 0:
            auxK = K
            robots += 1

    print(robots)


