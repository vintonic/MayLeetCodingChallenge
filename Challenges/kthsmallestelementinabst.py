# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        def in_order(root):
            if root is None:
                return []
            in_left = in_order(root.left)
            root_val = [root.val]
            in_right = in_order(root.right)
            return in_left + root_val + in_right
        
        return in_order(root)[k - 1]
