class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        

        count = [0]* (max(nums)+1)

        for e in nums:
            count[e] += 1

    
        sorted_arr = []
        for i,v in enumerate(count):
            while v > 0:
                sorted_arr.append(i)
                v -= 1

        hm = {}
        for i,e in enumerate(sorted_arr):
            if e not in hm:
                hm[e] = i

        
        for i in range(len(nums)):
            sorted_arr[i] = hm[nums[i]]
        return sorted_arr

        
