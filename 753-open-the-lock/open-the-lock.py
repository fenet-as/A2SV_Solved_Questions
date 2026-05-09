class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        

        visited = set(deadends)


        q = deque(["0000"])

        move = 0
        if "0000" in visited:
            return -1
        
        visited.add("0000")

        while q:
            for _ in range(len(q)):
                curr = q.popleft()

                if curr == target:
                    return move

               

                cr = list(curr)

                for i in range(4):
                    for s in [1,-1]:
                        
                        nc = (int(cr[i]) + s)%10
                        ncr = cr.copy()
                        ncr[i] = str(nc)
                        cur = ''.join(ncr)

                        if cur not in visited:
                            visited.add(cur)
                            q.append(cur)
            move += 1

        return -1

                    

