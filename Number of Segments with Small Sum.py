n,s = map(int,input().split())

arr = list(map(int,input().split()))

j = 0
sm = 0
ct = 0

for i in range(n):
  sm += arr[i]

  while sm > s:
    sm -= arr[j]
    j += 1

  ct += (i-j+1)
print(ct)
