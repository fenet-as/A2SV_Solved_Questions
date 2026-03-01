n,s = map(int,input().split())
arr = list(map(int,input().split()))

sm = 0
i = 0
j = 0
ct = 0


for i in range(n):
  while sm < s and j < n:
    sm += arr[j]
    j += 1
  

  if sm >= s:
    ct += n - j + 1
  sm -= arr[i]
  i += 1



print(ct)
