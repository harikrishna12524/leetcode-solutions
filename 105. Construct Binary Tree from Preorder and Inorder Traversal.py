# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        orderMap = {}
        for i in range(len(inorder)):
            orderMap[inorder[i]] = i
        
        def getTree(pre_ord):
            if(len(pre_ord) < 1):
                return None

            root = TreeNode(pre_ord[0])
            leftnodes = []
            rightnodes = []
            rootNodePos = orderMap[pre_ord[0]]
            for i in range(1, len(pre_ord)):
                if(orderMap[pre_ord[i]] < rootNodePos):
                    leftnodes.append(pre_ord[i])
                else:
                    rightnodes.append(pre_ord[i])

            root.left = getTree(leftnodes)
            root.right = getTree(rightnodes)
            return root
        return getTree(preorder)