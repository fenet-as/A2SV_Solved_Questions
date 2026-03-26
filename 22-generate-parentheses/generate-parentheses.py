class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        path = []
        res = []

                    
        def helper(hml,hmr):
            if len(path) == 2*n:
                res.append(''.join(path[:]))
                return 
            
            if hml < n:
                hml += 1
                path.append("(")
                helper(hml,hmr)
                path.pop()
                hml -= 1

            if hmr < hml:
                hmr += 1
                path.append(")")
                helper(hml,hmr)
                path.pop()
                hmr -= 1
            return 

        helper(0,0)
        return res
            


             

            