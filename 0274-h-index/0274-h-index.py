class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()

        i = len(citations)-1
        ct = 0
        while i >= 0 and citations[i] >= ct+1:
            i -= 1
            ct += 1
        return ct