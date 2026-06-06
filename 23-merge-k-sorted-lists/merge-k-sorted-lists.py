import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        

        def trav_ll(h,heap):

            while h:
                heap.append(h.val)
                h = h.next

        
        for h in lists:
            trav_ll(h,heap)

        # print(heap)
        heap.sort()



        dummy = ListNode(0)
        head = dummy
        

        for e in heap:
            head.next = ListNode(e)
            head = head.next
        return dummy.next




        