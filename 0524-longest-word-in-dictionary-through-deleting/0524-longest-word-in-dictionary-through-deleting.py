class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        

        words = []


        for w in dictionary:
            i = 0
            j = 0
            while j < len(s) and i < len(w):
                if w[i] == s[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            if i >= len(w):
                words.append(w)
        words.sort()
        words.sort(key=lambda x:len(x),reverse= True)

        if not words:
            return ""

        return words[0]            