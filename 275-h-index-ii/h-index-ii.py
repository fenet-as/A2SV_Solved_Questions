class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations)-1
        ans = 0

        def possible(ind):
            val = len(citations)-ind
            return citations[ind] >= val 

        while left <= right:
            mid = left + (right-left )//2

            if possible(mid):
                ans = len(citations) - mid
                right = mid-1
                
            else:
                left = mid + 1
                

        return ans