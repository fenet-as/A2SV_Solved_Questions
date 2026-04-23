from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)

        white, grey, black = 0, 1, 2
        colors = [white] * numCourses

        for i in range(numCourses):
            if colors[i] != white:
                continue

            stack = [(i, False)]  # (node, processed_children?)

            while stack:
                node, processed = stack.pop()

                if processed:
                    colors[node] = black
                    continue

                if colors[node] == grey:
                    return False

                if colors[node] == black:
                    continue

                colors[node] = grey
                stack.append((node, True))  # come back later

                for nei in adj[node]:
                    if colors[nei] == grey:
                        return False
                    if colors[nei] == white:
                        stack.append((nei, False))

        return True