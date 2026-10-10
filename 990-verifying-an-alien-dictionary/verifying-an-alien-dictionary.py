class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        orders = defaultdict(str)
        i = 0
        for e in order:
            orders[e] = i
            i += 1


        def compare(w1,w2):
            i = 0
            while i < len(w1) and i < len(w2):
                if orders[w1[i]] < orders[w2[i]]:return True
                elif orders[w1[i]] > orders[w2[i]]:return False
                i += 1
            
            if len(w1) > len(w2):return False
            return True

        
        j = 0
        while j < len(words)-1:
            if not compare(words[j], words[j+1]):
                return False
            j += 1
        return True

        
      

        

