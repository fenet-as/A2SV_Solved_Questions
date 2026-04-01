class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        left = 1
        right = max(piles)
        ans = -1

        # def possible(k):
        #     t = 0

        #     for e in piles:
        #         if e <= k:
        #             t += 1
        #         else:
        #             c = e
        #             while c > k:
        #                 c -= k
        #                 t += 1
        #             t += 1
        #     print("t ",t)
        #     if t > h:
        #         return False
        #     return True

        def possible(k):
            t = 0
            for e in piles:
                t += ceil(e/k)  # ceil division

            return t <= h

        while left <= right:
            mid = left + (right-left)//2
            # print(mid)

            if possible(mid):
                ans = mid
                right = mid-1
                # print("ans ",ans)
            
            else:
                left = mid + 1 
            
        return ans 