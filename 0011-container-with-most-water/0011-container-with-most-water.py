class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1

        mx = 0
        while i < j:
            area = min(height[i],height[j]) * (j - i)
            mx = max(mx,area)

            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
        return mx

