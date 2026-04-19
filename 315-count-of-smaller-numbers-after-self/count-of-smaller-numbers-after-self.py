class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0]* len(nums)

        for i,v in enumerate(nums):
            nums[i] = (i,v)
        def merge(arr1,arr2):
            i = 0
            j = 0

            merged = []

            rc = 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i][1] <= arr2[j][1]:
                    res[arr1[i][0]] += rc
                    merged.append(arr1[i])
                    i += 1
                elif arr2[j][1] < arr1[i][1]:
                    merged.append(arr2[j])
                    rc += 1
                    j += 1

            while i < len(arr1):

                res[arr1[i][0]] += rc
                merged.append(arr1[i])
                i += 1
            
            while j < len(arr2):
                merged.append(arr2[j])
                j += 1


            return merged
                  

        def sort(arr):
            if len(arr) == 1:
                return arr
            m = len(arr)//2
            left = sort(arr[:m])
            right = sort(arr[m:])

            return merge(left,right)

        sort(nums)
        return res