n = int(input())
arr = list(map(int,input().split()))


arr = sorted(arr)
j = 0
i = 0

while i < n and  j < n:
  curr = j + 1
  while i < n and arr[i] < curr:
    i += 1

  if i < n and arr[i] >= curr :
    j += 1
    i += 1


print(j)
