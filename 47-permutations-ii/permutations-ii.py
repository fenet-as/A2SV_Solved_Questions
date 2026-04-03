class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        # st = defaultdict(int)
        # ct = Counter(nums)
        used = [False] * len(nums)
        
        def explore():
            if len(path) == len(nums):
                if path not in res:
                    res.append(path[:])
                return 

            for i in range(len(nums)):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue 
                
                path.append(nums[i])
                # print(path)
                used[i] = True
                explore()
                path.pop()
                # print(path)
                used[i] = False
            return

        explore()
        return res

            

                