class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        

        #  calculate the not nested

        stack = []

        for e in s:
            if e == "(":
                stack.append(e)
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                    stack.append("1")
                else:
                    stack.append(e)
            
        # sum the not nested

        # print(stack)
        i = 0
        new = []
        while i < len(stack):
            if stack[i].isdigit():
                sm = 0
                while i < len(stack) and stack[i].isdigit():
                    sm += 1
                    i += 1
                new.append(sm)
                
            else:
                new.append(stack[i])
                i += 1
     
        m = 1
        res = 0
        for e in new:
            if e == "(":
                m *= 2
            elif e == ")":
                m //= 2
            else:
                res += m*e
        return res

            

        

