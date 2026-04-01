class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        ind = [(sum(mat[i]),i) for i in range(len(mat))]

        ind.sort(key = lambda x:(x[0],x[1]))

        res = []
        i = 0
        while len(res) < k:
            res.append(ind[i][1])
            i += 1
        return res






