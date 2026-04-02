import bisect

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        

        left = 0
        right = max(max(houses),max(heaters))

      

        heaters.sort()

        def possible(r):

            for e in houses:
                ind = bisect.bisect(heaters,e)
                if ind == 0:
                    rng = heaters[ind] - e
                elif ind == len(heaters):
                    rng = e - heaters[ind-1] 
                else:
                    rng = min(e - heaters[ind-1],heaters[ind] - e)
                if rng > r:
                    return False 

            return True
        ans = -1


        while left <= right:
            mid = left + (right -left )//2

            if possible(mid):
                ans = mid
                right = mid -1
            else:
                left = mid + 1
        return ans
        