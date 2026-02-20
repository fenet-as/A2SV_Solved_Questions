class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        n = len(nums)

        res = []
        for count in freq:
            if freq[count] > n/3:
                res.append(count)

        return res