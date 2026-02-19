n = int(input())
arr = list(map(int,input().split()))

arr.sort()
h = n//2
if n%2 == 0:
  print(arr[h-1])
else:
  print(arr[h])
