class Solution:
    def maxDepth(self, s: str) -> int:
        '''
        
        '''


        stack = []

        mx = float('-inf')
        for e in s:
            if e == "(":
                stack.append(e)
                mx = max(mx,len(stack))
            elif e == ")":
                if stack:stack.pop()

        if mx == float('-inf'):return 0
            
        return mx

        