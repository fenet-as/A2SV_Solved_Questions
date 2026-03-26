class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        bucket = [0]*k

        nums.sort(reverse = True)
        # print(sum(nums))
        if sum(nums) % k:
            return False


        div = sum(nums)//k

        if nums and nums[0] > div:
            return False
        
        def choose(i):
            nonlocal div
        
            if i == len(nums):
                return all(bucket[i] == div for i in range(k))

            for j in range(k):
                if j > 0 and bucket[j] == bucket[j-1]:
                    continue
                if bucket[j] + nums[i] <= div:
                    bucket[j] += nums[i]
                   
                    if choose(i+1):
                        return True
                    
                    bucket[j] -= nums[i]
            
            return False

        
        return choose(0)
