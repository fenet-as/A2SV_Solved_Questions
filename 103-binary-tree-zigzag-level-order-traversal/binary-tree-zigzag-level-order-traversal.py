# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = rightt
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        q = deque([root])

        res = []
        d = 1
        while q:
            arr = []

            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                arr.append(node.val)

            if d == 1:
                res.append(arr)
            else:
                res.append(list(reversed(arr)))
            
            d *= -1
        return res
                

