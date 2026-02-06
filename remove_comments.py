class Solution:
    def removeComments(self, source: List[str]) -> List[str]:

        res = []
        in_block = False
        new_line = []

        for line in source:
            if not in_block:
                new_line = []
            i = 0

            while i < len(line):
                if not in_block:
                    if i+1 < len(line) and line[i:i+2] == "//":
                        break
                    elif i+1 < len(line) and line[i:i+2] == "/*":
                        in_block = True
                        i += 2
                    else:
                        new_line.append(line[i])
                        i += 1

                else:
                    if i+1 < len(line) and line[i:i+2] == "*/":
                        in_block = False
                        i += 2
                    else:
                        i += 1
            if new_line and not in_block:
                res.append(''.join(new_line))
        return res 
                



