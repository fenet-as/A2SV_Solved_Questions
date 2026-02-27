
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = defaultdict(int)

        i = 0
        max_size = 0
        for j in range(len(s)):
            count[s[j]] += 1

            while ((j-i+1)  - max(count.values())) > k:
                count[s[i]] -= 1
                if count[s[i]] == 0:
                    del count[s[i]]
                i += 1
            max_size = max(max_size, j-i+1)
            
        return max_size


            
