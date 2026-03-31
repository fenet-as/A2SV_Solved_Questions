class Solution:
    def mySqrt(self, x: int) -> int:
        
        i = 0
        j = x
        ans = -1

        while i <= j:
            m = i + (j-i)//2

            if m*m <= x:
                ans = m
                i = m+1
            else:
                j = m-1
        return ans
