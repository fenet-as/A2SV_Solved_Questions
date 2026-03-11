class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mx = deque()
        mn = deque()

        l = 0

        mxl = 0
        for r in range(len(nums)):
            while mn and nums[mn[-1]] > nums[r]:
                mn.pop()
            mn.append(r)

            while mx and nums[mx[-1]] < nums[r]:
                mx.pop()
            mx.append(r)

            while mn and mx and nums[mx[0]] - nums[mn[0]] > limit:
                if mx[0] <= l:
                    mx.popleft()
                if mn[0] <= l:
                    mn.popleft()
                l += 1

            if mx and mn:
                mxl = max(mxl,r - l+1)


        return mxl



