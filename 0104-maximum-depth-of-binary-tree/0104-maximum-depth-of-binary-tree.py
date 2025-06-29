# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxDepthSearch(self, root: Optional[TreeNode], distance: Optional[int]) -> int:
        if root == None:
            return distance
        distance = distance + 1
        distance_left = self.maxDepthSearch(root.left, distance)
        distance_right = self.maxDepthSearch(root.right, distance)
        if distance_left > distance_right:
            distance = distance_left 
        else: 
            distance = distance_right
        return distance

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        distance_left = self.maxDepthSearch(root.left, 1)
        distance_right = self.maxDepthSearch(root.right, 1)
        if distance_left > distance_right:
            return distance_left 
        else: 
            return distance_right
        
        