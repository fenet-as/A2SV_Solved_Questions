class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def FindPerm(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for j in range(len(nums)):
                if nums[j] in  path:
                    continue

                path.append(nums[j])
                FindPerm(path)
                path.pop()
            return

        FindPerm([]) 
        return res   