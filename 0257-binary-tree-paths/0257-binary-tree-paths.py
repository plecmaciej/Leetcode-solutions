# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def binaryTreeNoding(self, root: Optional[TreeNode], nodes_string: Optional[str], paths_list: Optional[list]) -> List[str]:
        if root == None:
            return paths_list
        nodes_string = nodes_string + "->" + str(root.val)
        if root.left == None and root.right == None:
            paths_list.append(nodes_string)
            return paths_list
        paths_list = self.binaryTreeNoding(root.left,nodes_string, paths_list)
        paths_list = self.binaryTreeNoding(root.right,nodes_string, paths_list)
        return paths_list

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root == None:
            return None
        nodes_string = str(root.val)
        paths_list = []
        if root.left == None and root.right == None:
            paths_list.append(nodes_string)
            return paths_list
        paths_list = self.binaryTreeNoding(root.left,nodes_string, paths_list)
        paths_list = self.binaryTreeNoding(root.right,nodes_string, paths_list)
        return paths_list