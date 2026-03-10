class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for e in s:
            if e == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(e)
        return ''.join(stack)
