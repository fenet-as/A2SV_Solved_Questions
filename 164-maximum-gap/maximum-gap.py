class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        mn,mx = min(nums), max(nums)
        n = len(nums)

        bs = max(1,(mx-mn)//(n-1))
        bc = (mx-mn)//bs+1

        bucket = [[float("inf"),float("-inf")]for _ in range(bc)]


        for e in nums:
            ind = (e-mn)//bs
            
            bucket[ind][0] = min(e,bucket[ind][0])
            bucket[ind][1] = max(e,bucket[ind][1])

        pmax = mn
        d = 0

        for bmin,bmax in bucket:
            if bmin == float("inf"):
                continue
            d = max(d,bmin - pmax)
            pmax = bmax
        return d

            

