#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        hm = Counter(a)
        hmb = Counter(b)
        
        for e in hmb:
            if e not in hm:
                return False
            elif hmb[e] > hm[e]:
                return False
            
        return True
