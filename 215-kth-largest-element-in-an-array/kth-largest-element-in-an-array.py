import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        """
        1,2,3,4,5,6

        """
        e = nums[0]
        for _ in range(len(nums)-k + 1):
            e = heapq.heappop(nums)

        return e