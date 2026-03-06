from collections import Counter

t = int(input())

for _ in range(t):
  n,l,r = map(int,input().split())
  arr = list(map(int,input().split()))


  total = n//2

  left_counter = Counter(arr[:l])
  right_counter = Counter(arr[l:])

  flips = abs(l-r)//2

  if l > r:
    left_counter,right_counter = right_counter , left_counter

  for left in left_counter:
    matching = min(left_counter[left],right_counter[left])
    total -= matching
    right_counter[left] -= matching

  duplicates = 0
  for right in right_counter:
    duplicates += right_counter[right]//2

  if flips - duplicates <= 0:
    print(total)
  else:
    print(total + (flips - duplicates))

  




