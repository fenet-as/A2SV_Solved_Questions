class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        

       
        res = []


        def bt(o,c,curr):
            if o == n and c == n:
                res.append(''.join(curr))
                return


            if o < n:
                    curr.append('(')
                    bt(o+1,c,curr)
                    curr.pop()
                
            if c < o:
                    curr.append(')')
                    bt(o,c+1,curr)
                    curr.pop()
        bt(0,0,[])
        return res
            

            
