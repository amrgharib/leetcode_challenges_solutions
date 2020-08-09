# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def root_inc(self, root, sum):
        if root == None:
            return 0
        n_path = 0

        if root.val == sum:
            n_path += 1
        n_path += self.root_inc(root.left, sum - root.val)
        n_path += self.root_inc(root.right, sum - root.val)

        return n_path

    def pathSum(self, root: TreeNode, sum: int) -> int:

        if root == None:
            return 0

        return self.root_inc(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
