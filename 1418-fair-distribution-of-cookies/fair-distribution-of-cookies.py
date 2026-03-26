class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        sm = [0]*k
        mx = float("inf")
        def helper(i):
            nonlocal mx

            if i >= len(cookies):
                mx = min(mx,max(sm))
                return 
            
            for j in range(k):

            
                sm[j] += cookies[i]
                if sm[j] <= mx:
                    helper(i+1)
                sm[j] -= cookies[i]
            
            
            return
                
        helper(0)
        return mx

