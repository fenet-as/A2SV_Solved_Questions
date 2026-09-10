# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ct = [0]
        def move(node):
            if node.right:
                move(node.right)
            
            if node.left:
                move(node.left)
            
            sm = 0
            cct = 0

            if node.left: 
                sm += node.left.val[0]
                cct += node.left.val[1]
             
            if node.right: 
                sm += node.right.val[0]
                cct += node.right.val[1]


            sm += node.val
            cct += 1

            avg = sm//cct

            if node.val == avg : ct[0] += 1
            node.val = [sm,cct]

        move(root)
        return ct[0]

            


            
   

            

            


