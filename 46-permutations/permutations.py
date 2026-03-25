class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        path = []
        seen = [False]*len(nums)
        def FindPerm():
            if len(path) == len(nums):
                res.append(path[:])
                return

            for j in range(len(nums)):
                if seen[j]:
                    continue

                seen[j] = True
                path.append(nums[j])
                FindPerm()
                path.pop()
                seen[j] = False
            return

        FindPerm() 
        return res   