"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder_with_list(self, root: 'Node', output: Optional[list]) -> List[int]:
        if root == None:
            return output
        for i in range(len(root.children)):
            output = self.postorder_with_list(root.children[i], output)
        output.append(root.val)
        return output

    def postorder(self, root: 'Node') -> List[int]:
        output = []
        return self.postorder_with_list(root, output)