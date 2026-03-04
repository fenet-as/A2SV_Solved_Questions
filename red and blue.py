t = int(input())
for _ in range(t):
  n = int(input())
  arr1 = list(map(int,input().split()))

  m = int(input())
  arr2 = list(map(int,input().split()))


  for i in range(1,n):
    arr1[i] += arr1[i-1]

  for i in range(1,m):
    arr2[i] += arr2[i-1]

  mx1 = max(0,max(arr1))
  mx2 = max(0,max(arr2))

  mx = mx1 + mx2
  
  print(mx)
  
