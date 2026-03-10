class DataStream:

    def __init__(self, value: int, k: int):
        self.ls = deque()
        self.k = k
        self.val = value
        self.ct = 0

    def consec(self, num: int) -> bool:
        if len(self.ls) >= self.k:
            rv = self.ls.popleft()
            if rv == self.val:
                self.ct -= 1
        self.ls.append(num)
        if num == self.val:
            self.ct += 1
        if len(self.ls) < self.k:
            return False
        if self.ct != self.k:
            return False
        else:
            return True

        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
'''
[4,4,3]
ct = 2
- if the size of ls is > k , popleft,before adding
'''
