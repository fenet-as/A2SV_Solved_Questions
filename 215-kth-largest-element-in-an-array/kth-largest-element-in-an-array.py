import random
from typing import List

class Solution:
    def findKthLargest(self, arr: List[int], k: int) -> int:
        target = len(arr) - k
        left, right = 0, len(arr) - 1

        while True:
            pivot = arr[random.randint(left, right)]

            # 3-way partition
            l, m, r = left, left, right

            while m <= r:
                if arr[m] < pivot:
                    arr[l], arr[m] = arr[m], arr[l]
                    l += 1
                    m += 1
                elif arr[m] > pivot:
                    arr[m], arr[r] = arr[r], arr[m]
                    r -= 1
                else:
                    m += 1

        

            if target < l:
                right = l - 1
            elif target > r:
                left = r + 1
            else:
                return pivot