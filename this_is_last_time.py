t = int(input())

for _ in range(t):
  n,k = map(int,input().split())
  arr = []
  for _ in range(n):
    l,r,rl = map(int,input().split())
    arr.append([l,r,rl])

  arr.sort(key=lambda x:x[0])

  # print(arr,k)

  

  for i in range(n):
    l,r,rl = arr[i]
    if l <= k <= r:
      k = max(rl,k)
      
    # print("k ",k)
  


  print(k)
  
