class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        
        hm = defaultdict(lambda :float("inf"))

        for i,v in enumerate(order):
            hm[v] = i

        s = list(s)
        s.sort(key= lambda x: hm[x])


        return ''.join(s)