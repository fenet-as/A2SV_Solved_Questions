class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # code
        
        i = 0

        st = set()
        max_size = 0
        for j in range(len(s)):
            while s[j] in st:
                st.remove(s[i])
                i += 1
            st.add(s[j])

            max_size = max(max_size,j - i + 1)
        return max_size
            