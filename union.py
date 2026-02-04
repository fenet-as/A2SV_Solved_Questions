class Solution:    
    def findUnion(self, a, b):
        # code here
        st1 = set(a)
        st2 = set(b)
        union = list(st1 | st2)
        return union
