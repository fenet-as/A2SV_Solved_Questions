class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        i = 0
        j = len(nums)-1
        c = nums[0]
        ans = nums[0]


        while i <= j:
            mid = i + (j-i)//2

            if nums[mid] < c:
                ans = nums[mid]
                j = mid - 1 
            else:
                i = mid + 1
            # print(nums[mid])
        return ans
