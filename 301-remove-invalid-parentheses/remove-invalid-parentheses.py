class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def check(s):
            stack = []

            for e in s:
                if e == ")":
                    if stack and stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                elif e == "(":
                    stack.append(e)
            if stack:
                return False
            return True

      
        res = set()
        def remove(s,i):
            if len(s) == 0 or  i == len(s):
                if check(s):
                    res.add(s)
                return

            for j in range(i,len(s)):
                if s[j] not in "()":
                    continue

                curr = s[:j] + s[j+1:]
                # if check(curr):
                #     res.add(curr)
          
                remove(curr,j)

            if check(s):
                res.add(s)

            return 

        remove(s,0)

        # ans = list(res)
        # ans.sort(key = lambda x:len(x),reverse = True)

        # print(res)
        if not res:
            return [""]
        # i = 1
        # while i < len(ans):
        #     if len(ans[i]) == len(ans[i-1]):
        #         i += 1
        #     else:
        #         break

        mxl = max(len(e) for e in res)


        
        return [e for e in res if len(e) == mxl]

        






                
            


