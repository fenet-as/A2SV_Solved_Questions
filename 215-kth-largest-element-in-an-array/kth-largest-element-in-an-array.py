class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k
        left, right = 0,len(nums)-1


        while True:
            p = random.randint(left, right)
            lw,rw,r = left,right,left
            pivot = nums[p]

            while r <= rw:
                if nums[r] < pivot:
                    nums[lw],nums[r] = nums[r], nums[lw]
                    lw += 1
                    r += 1
                
                elif  nums[r] > pivot: 
                    nums[rw],nums[r] = nums[r],nums[rw]
                    rw -= 1
                else:
                    r += 1
            
            if k < lw:
                right = lw-1
            elif k > rw:
                left = rw + 1
            else:
                return pivot


