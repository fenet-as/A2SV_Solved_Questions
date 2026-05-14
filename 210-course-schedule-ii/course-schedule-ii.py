class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        ct = [0]*numCourses

        for a,b in prerequisites:
            graph[b].append(a)
            ct[a] += 1
        q = deque()
        for i in range(len(ct)):
            if ct[i] == 0:
                q.append(i)

        order = []


        while q:
            curr = q.popleft()
            order.append(curr)

            for nei in graph[curr]:
                ct[nei] -= 1

                if ct[nei] == 0:
                    q.append(nei)

        if len(order) < numCourses:
            return []
        return order

