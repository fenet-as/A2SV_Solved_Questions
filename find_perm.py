from collections import defaultdict;
t = int(input())

for _ in range(t):
  n = int(input())


  mat = []
  for _ in range(n):
    arr = list(map(int,list(input())))
    mat.append(arr)

  hm = defaultdict(set)

  for i in range(n):
    for j in range(i+1,n):

      if mat[i][j] == 1:
        hm[j+1].add(i+1)
      else:
        hm[i+1].add(j+1)

      

  res = [0]*n

  for i in range(n):
    ind = len(hm[i+1])
    res[ind] = i+1

  print(*res)
