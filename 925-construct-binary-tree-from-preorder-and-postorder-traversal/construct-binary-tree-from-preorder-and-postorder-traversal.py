# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        hm = {}

        for i,v in enumerate(postorder):
            hm[v] = i


        def build(l1,r1,l2,r2):

            if l1 > r1:
                return None

            if l1 == r1:
                return TreeNode(preorder[l1])

            pri = l1+1
            psi =  hm[preorder[pri]]

            d = psi - l2 + 1

     

            root = TreeNode(preorder[l1])

            root.left = build(pri,pri+d-1,l2,psi)
            root.right = build(pri+d,r1,psi+1,r2-1)

            return root


        return build(0,len(preorder)-1,0,len(postorder)-1)
       


             

        