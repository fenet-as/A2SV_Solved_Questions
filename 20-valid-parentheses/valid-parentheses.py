class Solution:
    def isValid(self, s: str) -> bool:
        


        stack = []
        for e in s:
            if e in "({[":
                stack.append(e)
            else:
                if stack:
                    if stack[-1] == '(' and e != ')':
                        return False
                    if stack[-1] == '{' and e != '}':
                        return False
                    if stack[-1] == '[' and e != ']':
                        return False
                    stack.pop()
                else:
                    return False
        if stack:return False
        return True