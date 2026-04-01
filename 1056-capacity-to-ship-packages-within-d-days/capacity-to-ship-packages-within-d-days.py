class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # print(sum(weights))


        left = max(weights)
        right = sum(weights)
        ans = -1

        def possible(w):
            d = 0
            curr_weight = 0

            for e in weights:
                if curr_weight + e > w:
                    d += 1
                    curr_weight = e
                else:
                    curr_weight += e
            if d+1 > days:
                return False
            return True



        while left <= right:

            mid = left + (right-left)//2

            if possible(mid):
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans
