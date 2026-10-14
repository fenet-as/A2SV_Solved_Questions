class Solution:
    def trap(self, height: list[int]) -> int:

        left_max = []
        _max = float('-inf')
        for e in height:
            _max = max(_max,e)
            left_max.append(_max)

        right_max = [0]*len(height)
        _max = float('-inf')
        for i,v in enumerate(reversed(height)):
            _max = max(_max,v)
            idx = (len(height)-1 - i)
            right_max[idx] = _max


        
        res = 0

        for i in range(len(height)):
            res += max(0,min(left_max[i],right_max[i]) - height[i])
        return res





