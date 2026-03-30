r, c = map(int, input().split())

mat = [list(input()) for _ in range(r)]


H = [[0]*c for _ in range(r)]
V = [[0]*c for _ in range(r)]

for i in range(r):
    for j in range(c-1):
        if mat[i][j] == '.' and mat[i][j+1] == '.':
            H[i][j] = 1

for i in range(r-1):
    for j in range(c):
        if mat[i][j] == '.' and mat[i+1][j] == '.':
            V[i][j] = 1


prefH = [[0]*(c+1) for _ in range(r+1)]
prefV = [[0]*(c+1) for _ in range(r+1)]

for i in range(1, r+1):
    for j in range(1, c+1):
        prefH[i][j] = (H[i-1][j-1]
                       + prefH[i-1][j]
                       + prefH[i][j-1]
                       - prefH[i-1][j-1])

        prefV[i][j] = (V[i-1][j-1]
                       + prefV[i-1][j]
                       + prefV[i][j-1]
                       - prefV[i-1][j-1])

def get(pref, r1, c1, r2, c2):
    if r1 > r2 or c1 > c2:
        return 0
    return (pref[r2][c2]
            - pref[r1-1][c2]
            - pref[r2][c1-1]
            + pref[r1-1][c1-1])

q = int(input())

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())

    
    sumH = get(prefH, r1, c1, r2, c2-1)

    sumV = get(prefV, r1, c1, r2-1, c2)

    print(sumH + sumV)
