# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def preorderTraversalList(self, root: Optional[TreeNode], output: List[int]) -> List[int]:
        if root == None:
            return output
        output.append(root.val)
        output = self.preorderTraversalList(root.left, output)
        output = self.preorderTraversalList(root.right, output)
        return output
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        return self.preorderTraversalList(root, output)
        