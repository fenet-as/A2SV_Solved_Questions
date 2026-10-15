class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        
        safe = set()
        for i in range(len(graph)):
            if graph[i] == []:
                safe.add(i)


        
    
        changed = True

        while changed:
            changed = False

            for i in range(len(graph)):
                if set(graph[i]) <= safe:
                    if i not in safe:
                        safe.add(i)
                        changed = True


        return sorted(list(safe))

                