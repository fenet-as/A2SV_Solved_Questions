t = int(input())

for _ in range(t):
  s = input()

  res = set()
  i = 0
  j = 1

  while i < len(s) and j < len(s):
    while j < len(s) and s[i] == s[j]:
      j += 1

    if (j - i) % 2 == 1:
      res.add(s[i])
    # print(i,j)
    i = j
    j += 1
  if i < len(s):
    res.add(s[i])
  
  res = list(res)
  res.sort()
  print( ''.join(res))
