class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        ans = -1

        def possible(w):
            d = 1
            curr = 0
            
            for e in weights:
                if curr + e > w:
                    d += 1
                    curr = e
                else:
                    curr += e
            return d <= days

            


        while left <= right:
            mid = left + (right-left)//2
            if possible(mid):
                ans = mid
                right = mid-1
            else:
                left = mid + 1
            
        return ans