class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if(sum(candies) < k):
            return 0

        
        left = 1
        right = max(candies)
        ans = 0

        def possible(m,k):
            count = 0

            for v in candies:
                count += (v//m)
            return count >= k


        while left <= right:
            mid = left + (right-left)//2

            if possible(mid,k):
                ans = mid
                left = mid+1
                

            else:
                right = mid-1
        return ans 


        #