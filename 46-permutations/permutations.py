class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        def FindPerm(path,i):
            if len(path) == len(nums):
                res.append(path[:])

            for j in range(len(nums)):
                if nums[j] in path:
                    continue

                else:
                    path.append(nums[j])
                    FindPerm(path,j)
                    path.pop()
            i += 1
            return

        FindPerm([],0)
        return res
