class RecentCounter:

    def __init__(self):
        self.st = deque()
        

    def ping(self, t: int) -> int:
        self.st.append(t)

        while self.st and self.st[0] < (t-3000):
            self.st.popleft()
        return len(self.st)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
