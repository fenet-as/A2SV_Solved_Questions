class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        '''

        
        '''
        
        res = []

        op = 0
        cl = 0

        i = 0
        j = 0

        while j < len(s):
            if s[j] == "(" : op += 1
            else:cl += 1

            if op == cl and op != 0:
                res.append(s[i+1:j])
            
                op = 0
                cl = 0
                i = j+1

            j += 1

        return ''.join(res)

            
            



