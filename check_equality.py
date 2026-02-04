from collections import Counter
class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        return Counter(a) == Counter(b)
    
