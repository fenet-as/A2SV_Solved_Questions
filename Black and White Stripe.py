t = int(input())

for _ in range(t):
  n,k = map(int,input().split())
  s = input()
  ctw = 0
  for i in range(k):
    if s[i] == "W":
      ctw += 1

  _min = ctw
  i = 0
  for j in range(k,n):
    if s[i] == "W":
      ctw -= 1
    
    if s[j] == "W":
      ctw += 1

    i += 1

    _min = min(ctw,_min)

  print(_min)

