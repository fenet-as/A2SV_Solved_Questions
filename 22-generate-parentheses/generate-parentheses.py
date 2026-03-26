class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        hm = {"(":0,")":0}
        path = []
        res = []

        def check(arr):
            stack = []

            for i in range(len(arr)):
                if stack: 
                    if arr[i] == "(":
                        stack.append(arr[i])
                    else:
                        if stack and stack[-1] == "(":
                            stack.pop()
                        else:
                            return False
                else:
                    stack.append(arr[i])
            if stack:
                return False
            return True

                    
        def helper():
            if len(path) == 2*n:
                if check(path):
                    res.append(''.join(path[:]))
                return 
            
            if hm["("] < n:
                hm["("] += 1
                path.append("(")
                helper()
                path.pop()
                hm["("] -= 1

            if hm[")"] < n:
                hm[")"] += 1
                path.append(")")
                helper()
                path.pop()
                hm[")"] -= 1
            return 

        helper()
        return res
            


             

            