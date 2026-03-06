n,k,q = map(int,input().split())


rec = [0]*200004
for _ in range(n):
  l,r = map(int,input().split())
  rec[l] += 1
  rec[r+1] -= 1

for i in range(1,len(rec)):
  rec[i] += rec[i-1]

good = [0]*200004

if rec[0] >= k:
  good[0] += 1

for i in range(1,len(good)):
  if rec[i] >= k:
    good[i] += 1
  good[i] += good[i-1]

  


res = []

for i in range(q):
  l,r = map(int,input().split())
  res.append(good[r] - good[l-1])



for e in res:
  print(e)







