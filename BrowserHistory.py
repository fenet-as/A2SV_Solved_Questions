class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None



class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = Node(homepage)
        

    def visit(self, url: str) -> None:
        new_node = Node(url)

        self.history.next = new_node
        new_node.prev = self.history

        self.history = self.history.next



    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.history.prev:
                self.history = self.history.prev
            else:
                return self.history.val
         

     
        return self.history.val
        

    def forward(self, steps: int) -> str:

        for i in range(steps):
            if self.history.next:
                self.history = self.history.next
            else:
                return self.history.val

        return self.history.val
       


        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
