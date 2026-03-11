# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        stack = []

        curr = head

        while curr:
            while stack and stack[-1].val < curr.val:
                stack.pop()
            
            stack.append(curr)
            curr = curr.next

        dummy = ListNode(0)
        dummy_head = dummy

        for e in stack:
            dummy.next = e
            dummy = dummy.next
        dummy.next = None

        return dummy_head.next
