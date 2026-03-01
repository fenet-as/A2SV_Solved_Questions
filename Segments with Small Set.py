from collections import defaultdict

n,k = map(int,input().split())
arr = list(map(int,input().split()))

st = defaultdict(int)


j = 0
ct = 0
for i in range(n):
  st[arr[i]] += 1

  while j < n and len(st) > k:
    st[arr[j]] -= 1
    if st[arr[j]] == 0:
      del st[arr[j]]
    j += 1
  ct += (i-j+1)

print(ct)

  
