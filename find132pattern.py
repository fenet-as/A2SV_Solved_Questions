class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] # stores possible j and the min before them
        _min = nums[0] # keeps track of the min before the next elemnt

        for e in  nums[1:]:
            while stack and e >= stack[-1][1]:
                stack.pop()

            if stack and  e < stack[-1][1] and e > stack[-1][0]:
                return True

            stack.append([_min,e])
            _min = min(e,_min)
        return False 
