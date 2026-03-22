# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        _sum = 0
        if root.left:
            if not root.left.left:
                _sum += 0
            else:
                if root.val % 2 == 0:
                    _sum += root.left.left.val

            if not root.left.right:
                _sum += 0
            else:
                if root.val % 2 == 0:
                    _sum += root.left.right.val

            
            
            

        if root.right:
            if not root.right.left:
                _sum += 0
            else:
                if root.val % 2 == 0:
                    _sum += root.right.left.val

            if not root.right.right:
                _sum += 0
            else:
                if root.val % 2 == 0:
                    _sum += root.right.right.val

        
        _sum += self.sumEvenGrandparent(root.left)
        _sum += self.sumEvenGrandparent(root.right)

        return _sum
        
        

            




