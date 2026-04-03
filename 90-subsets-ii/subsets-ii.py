class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = [[]]
        path = []
        nums.sort()
        
        
        def explore(i):
            if i == len(nums):
                return

          

            for j in range(i,len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue

                path.append(nums[j])
                res.append(path[:])
                explore(j+1)
                path.pop()

            return 
        explore(0)
        return res



            
