# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDepth(self, root: Optional[TreeNode], depth) -> int:
        queue = deque()
        while(True):

            if root.left == None and root.right == None:
                return depth

            else: 
                if root.left != None:
                    queue.append((root.left, depth + 1))
                if root.right != None:
                    queue.append((root.right, depth +1))
            
            root, depth = queue.popleft()

        return depth 

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return self.findDepth(root, 1)