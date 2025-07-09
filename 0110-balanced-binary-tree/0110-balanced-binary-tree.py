# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def returnDepth(self, root: Optional[TreeNode], depth: int) -> int:
        if root is None:
            return depth - 1 
        right_depth = depth
        left_depth = depth

        right_depth = self.returnDepth(root.right, depth+1)
        left_depth = self.returnDepth(root.left, depth+1)
        if right_depth > left_depth:
            return right_depth
        else:
            return left_depth

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if self.isBalanced(root.left) == False:
            return False
        if self.isBalanced(root.right) == False:
            return False
        left_depth = self.returnDepth(root.left, 1)
        right_depth = self.returnDepth(root.right, 1)
        if abs(left_depth - right_depth) > 1:
            return False
        else:
            return True
        


        