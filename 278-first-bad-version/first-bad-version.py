# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        i = 1
        j = n
        ans = -1

        while i <= j:
            m = i + (j-i)//2

            if isBadVersion(m):
                ans = m
                j = m-1
            else:
                i = m +1

        return ans 