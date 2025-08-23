# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDepth(self, root: Optional[TreeNode], depth) -> int:
        if root.left != None:
            left_depth = self.findDepth(root.left,depth+1)
            if root.right != None:
                right_depth = self.findDepth(root.right,depth+1)
                if left_depth > right_depth:
                    return right_depth
            return left_depth
        elif root.right != None:
            depth = self.findDepth(root.right,depth+1)
        else:
            return depth

        return depth 

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return self.findDepth(root, 1)