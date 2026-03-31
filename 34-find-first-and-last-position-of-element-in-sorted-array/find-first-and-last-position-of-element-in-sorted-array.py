class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        

        def first_occurence(target):
            l = 0
            r = len(nums)-1
            ans = -1
            while l <= r:
                m = (l+r)//2

                if nums[m] == target:
                    ans = m
                    r = m-1
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m-1

            return ans

        def last_occurence(target):
            l = 0
            r = len(nums)-1
            ans = -1
            while l <= r:
                m = (l+r)//2

                if nums[m] == target:
                    ans = m
                    l = m+1
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m-1

            return ans

        last = last_occurence(target)
        first = first_occurence(target)

        return [first,last]

        

                