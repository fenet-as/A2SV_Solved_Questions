class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None
        self.prev = None


class MyCircularDeque:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.k = k
        self.size = 0

    def insertFront(self, value: int) -> bool:
        
        if self.size == self.k:
            return False

        new = Node(value)


        

        if not self.head:
            self.head = self.tail = new
        else:
            self.head.prev = new
            new.next = self.head
            self.head = new

        self.size += 1
        return True

    
    def insertLast(self, value: int) -> bool:

        
        if self.size == self.k:
            return False

        
        new = Node(value)

        if not self.tail:
            self.head = self.tail = new
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new

        self.size += 1
        return True


    def deleteFront(self) -> bool:
        if not self.head:
            return False

    
        self.head = self.head.next
        if self.head:
            self.head.prev = None

        else:
            self.tail = self.head = None

        self.size -= 1
        return True
        

    def deleteLast(self) -> bool:

        if not self.tail:
            return False

        
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.tail = self.head = None

        self.size -= 1
        return True
        

    def getFront(self) -> int:
        if not self.head:
            return -1
        return self.head.val
        

    def getRear(self) -> int:
        if not self.tail:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return  not self.head
        

    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
