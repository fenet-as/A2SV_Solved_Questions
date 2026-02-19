class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        res = []
        for i in range(len(arr),0,-1):
            for j in range(len(arr)):
                if arr[j] == i:
                    arr[:j+1] = reversed(arr[:j+1])
                    res.append(j+1)
                    break
            arr[:i] = reversed(arr[:i])
            res.append(i)
        return res

