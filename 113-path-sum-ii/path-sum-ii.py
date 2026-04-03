# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        path = []

        def explore(node,cs):
            if not node:
                return 
            
            if not node.left and not node.right:
                path.append(node.val)
                # print(path)
                cs += node.val
                if cs  == targetSum:
                    res.append(path[:])
                path.pop()
                cs -= node.val
                # print(path)
                # print("leaf")
                return
            

            path.append(node.val)
            # print(path)
            cs += node.val
            explore(node.right,cs)
            cs -= node.val
            path.pop()
            # print(path)

            path.append(node.val)
            cs += node.val
            # print(path)
            explore(node.left,cs)
            cs -= node.val
            path.pop()
            # print(path)

        explore(root,0)
        return res


            
