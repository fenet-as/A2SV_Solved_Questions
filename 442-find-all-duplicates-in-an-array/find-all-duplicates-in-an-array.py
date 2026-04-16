class Solution:
    def findDuplicates(self, arr: List[int]) -> List[int]:
        res = []

        for val in arr:
            ind = abs(val)-1
            if arr[ind] < 0:
                res.append(abs(val))
            else:
                arr[ind] *= -1
        return res
