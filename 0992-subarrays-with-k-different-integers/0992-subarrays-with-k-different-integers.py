class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        ct1 = 0
        n = len(nums)
        sm1 = defaultdict(int)
        l = 0
        for i in range(n):
            sm1[nums[i]] += 1

            while len(sm1) > k:
                sm1[nums[l]] -= 1
                if sm1[nums[l]] == 0:
                    del sm1[nums[l]]
                l += 1

            ct1 += (i-l+1)



        
        ct2 = 0

        sm2 = defaultdict(int)
        l = 0
        for i in range(n):
            sm2[nums[i]] += 1

            while len(sm2) > k-1:
                sm2[nums[l]] -= 1
                if sm2[nums[l]] == 0:
                    del sm2[nums[l]]
                l += 1

            ct2 += (i-l+1)

        return ct1 - ct2

        


            