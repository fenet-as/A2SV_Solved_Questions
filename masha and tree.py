
t = int(input())

ct = [0]

def check(arr):
  i = 1
  while i < len(arr):
    if arr[i-1] > arr[i]:
      return False
    i += 1
  return True

def merge(a1,a2):
  
  if a1[0] > a2[0]:
    ct[0] += 1
    return a2+a1
  
  return a1 + a2

def Sort(arr):
  if len(arr) == 1:
    return arr

  if len(arr) == 2:
    if arr[0] > arr[1]:
      arr[0],arr[1] = arr[1],arr[0]
      ct[0] += 1
    return arr
  m = len(arr)//2
  left = Sort(arr[:m])
  right = Sort(arr[m:])

  return merge(left,right)
  


for _ in range(t):
  
  n = int(input())

  arr = list(map(int,input().split()))

  arr = Sort(arr)
  # print(arr)

  if check(arr):
    print(ct[0])
  else:
    print(-1)
  ct[0] = 0



