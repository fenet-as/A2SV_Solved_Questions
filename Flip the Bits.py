t = int(input())

for _ in range(t):
  n = int(input())
  a1 = list(map(int,list(input())))
  a2 = list(map(int,list(input())))

  
  i = n-1
  ct0 = a1.count(0)
  ct1 = a1.count(1)

  cr = [0,1]
  
  possible = True

  while i >= 0:
    prev = a1[i]
    if a1[i] == 1:
      a1[i] = cr[1]
    else:
      a1[i] = cr[0]

    
    if a2[i] != a1[i]:
      if ct0 == ct1:
        cr[0],cr[1] = cr[1],cr[0]
      else:
        possible = False
        print("NO")
        break
    
    if prev == a1[i]:
      if a1[i] == 0:
        ct0 -= 1
      else:
        ct1 -= 1
    else:
      if a1[i] == 0:
        ct1 -= 1
      else:
        ct0 -= 1
       
    i -= 1
   
  if possible:
    print("YES")


      
