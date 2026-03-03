class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left_pdt = []
        cp = 1
        for i in range(n):
            cp *= nums[i]
            left_pdt.append(cp)

        right_pdt = []

        cp = 1
        for j in range(n-1,-1,-1):
            cp *= nums[j]
            right_pdt.append(cp)

        right_pdt.reverse()



        res = []

        for i in range(n):
            rp = 1 if i+1 >= n else right_pdt[i+1]
            lp = 1 if i-1 < 0 else left_pdt[i-1]
            res.append(rp*lp)
        return res 