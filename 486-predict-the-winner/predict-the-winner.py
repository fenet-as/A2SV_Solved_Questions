class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def explore(i,j):
            if i == j:
                return nums[i]

            left = nums[i] - explore(i+1,j)
            right = nums[j] - explore(i,j-1)
            return max(left,right)

        return explore(0,len(nums)-1) >= 0