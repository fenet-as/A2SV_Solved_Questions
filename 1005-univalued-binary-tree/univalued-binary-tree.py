# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        

        q = deque([root])

        if not root:
            return True

        while q:
            curr = q.popleft()

            if curr.left :
                if curr.left.val != root.val:
                    return False
                q.append(curr.left)

            if curr.right:
                if curr.right.val != root.val:
                    return False
                q.append(curr.right)
            
        return True