tc = int(input())
for t in range(1, tc + 1):
    n, k, p = map(int, input().split())
    s = []
    for i in range(n):
        b = list(map(int, input().split()))
        v = [0]
        for j in range(k):
            v.append(v[-1] + b[j])
        s.append(v)
    d = []
    d.append([0] * (p + 1))

    for j in range(min(k, p) + 1):
        d[0][j] = s[0][j]
    
    for i in range(1, n):
        d.append([0] * (p + 1))
        for j in range(p + 1):
            print(d)
            d[i][j] = d[i - 1][j]
            print(d)
            for l in range(min(k, j) + 1):
                v = d[i - 1][j - l] + s[i][l]
                print(v)
                if d[i][j] < v:
                    d[i][j] = v
    print('Case #{}: {}'.format(t, d[n - 1][p]))
