class Solution:
    def decodeString(self, s: str) -> str:

        def extract(s,i,k):

            si = i + 1

            word = []
            j = si

            while j < len(s) and s[j] != "]":
                if s[j].isdigit():
                    m = j
                    while s[m].isdigit():
                        m += 1
                    kt = int(s[j:m])
                    v = extract(s,m,kt)
                    word.append(v[0])
                    j = v[1]
                else:
                    word.append(s[j])
                j += 1
            
            words = ''.join(k*word)
            # words = ""
            return [words,j]
        
            

        
        res = []

        i = 0
        while i < len(s):
            val = s[i]
            if val.isdigit():
                m = i
                while s[m].isdigit():
                    m += 1
                k = int(s[i:m])
                v = extract(s,m,k)

                res.append(v[0])
                i = v[1]
           
            else:
                res.append(s[i])
            i += 1
        return ''.join(res)

