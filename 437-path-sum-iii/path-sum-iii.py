# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        ct = 0
        path = []
        def move(node,cs):
            nonlocal ct
            if not node:
                return 
            # if not node.left and not node.right:
            #     cs += node.val
            #     path.append(node.val)
            #     print(path)

            # if cs == targetSum:
            #     ct += 1

                # cs -= 1
                # path.pop()
                # print(path)
                

                # # print(path)
                # print("leaf") 

                # return 

            if cs+node.val == targetSum:
                ct += 1

            # path.append(node.val)
            # cs += node.val
            # print(path)
            move(node.left,cs+node.val)
            # cs -= node.val
            # path.pop()
            # print(path)

            # path.append(node.val)
            # cs += node.val
            # print(path)
            move(node.right,cs+node.val)
            # path.pop()
            # cs -= node.val
            # print(path)
            return 


        def explore(node,cs):
            nonlocal ct
            if not node:
                return 

            move(node,cs)

            explore(node.left,cs)
            print("first iter")
            explore(node.right,cs)
            print("second iter")
            return

        explore(root,0)
        return ct

        
