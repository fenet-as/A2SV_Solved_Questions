class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []

        mx = 0

        for i in range(len(heights)+1):
            curr = 0
            if i < len(heights):
                curr = heights[i]

            
            while stack and heights[stack[-1]] > curr:
                h = heights[stack.pop()]
                l = -1 if not stack else stack[-1]
                w = i - l-1 
                
                mx = max(h*w,mx)
            stack.append(i)
        return mx

