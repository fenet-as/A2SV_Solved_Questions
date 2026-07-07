class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        fo = -1 

        while  l <= r:
            m = (l+r)//2
            if nums[m] < target:
                l = m+1 
            elif nums[m] > target:
                r = m-1
            else:
                fo = m
                r = m-1
            print(l,r,m)

        l = 0
        r = len(nums)-1
        lo = -1 
        while  l <= r:
            m = (l+r)//2
            if nums[m] < target:
                l = m+1 
            elif nums[m] > target:
                r = m-1
            else:
                lo = m
                l = m+1

        return [fo,lo]



