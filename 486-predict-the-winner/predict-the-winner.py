class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        from functools import lru_cache

        # @lru_cache(None)
        def explore(i, j):
            if i == j:
                return nums[i]

            pick_left = nums[i] - explore(i+1, j)
            pick_right = nums[j] - explore(i, j-1)

            return max(pick_left, pick_right)

        return explore(0, len(nums)-1) >= 0