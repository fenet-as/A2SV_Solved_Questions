t = int(input())
for _ in range(t):
  n = int(input())
  arr = list(map(int,input().split()))

  res = []
  res.append(arr[0])
  i = 1
  dr = 1
  if arr[0] > arr[1]:
    dr = 0


  while i < n-1:
    if arr[i] > arr[i+1] and dr == 1:
      res.append(arr[i])
      dr = 0

    elif arr[i] < arr[i+1] and dr == 0:
      res.append(arr[i])
      dr = 1
    i += 1
  res.append(arr[i])

  print(len(res))
  print(*res)



    



