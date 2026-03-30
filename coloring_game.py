import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    
    total = 0
    max_val = A[-1]
    
    for k in range(n):
        c = A[k]
        
        threshold = max(c, max_val - c)
        
        j = k - 1
        
        for i in range(k):
            while j > i and A[i] + A[j] > threshold:
                j -= 1
            
            total += k - max(i, j) - 1
    
    print(total)
  
