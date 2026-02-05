# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeft(self, root: Optional[TreeNode], summary: int) -> int:
        if root is None:
            return summary
        if root.left == None and root.right == None:
            print(summary, root.val)
            summary = summary + root.val
        summary = self.sumOfLeft(root.left, summary)
        if root.right is not None:
            if root.right.right is not None or root.right.left is not None:
                summary = self.sumOfLeft(root.right, summary)
        return summary

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        summary = 0
        if root == None:
            return summary
        if root.left == None and root.right == None:
            return summary
        summary = self.sumOfLeft(root, summary)
        return summary
        