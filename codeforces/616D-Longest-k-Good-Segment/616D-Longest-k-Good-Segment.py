import sys
input = sys.stdin.readline 

n,k = map(int,(input().split()))

arr = list(map(int,input().split()))

i = 0
mx = [0,0,0]
st = {}

for j in range(n):
  if arr[j] not in st:
    st[arr[j]] = 1
  else:
    st[arr[j]] += 1

  while i < n and len(st) > k:
    st[arr[i]] -= 1
    if st[arr[i]] == 0:
      del st[arr[i]]
    i += 1

  if mx[2] < j-i+1:
    mx[2] = j-i+1
    mx[0]=i+1
    mx[1] = j+1


print(mx[0],mx[1])