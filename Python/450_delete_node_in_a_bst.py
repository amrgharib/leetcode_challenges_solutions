# # Top solution
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
#         if root:
#             if key < root.val:
#                 root.left = self.deleteNode(root.left, key)
#             elif key > root.val:
#                 root.right = self.deleteNode(root.right, key)
#             else:
#                 if root.left is None: return root.right
#                 elif root.right is None: return root.left
#                 nxt = root.right
#                 while nxt.left:
#                     nxt = nxt.left
#                 root.val = nxt.val
#                 root.right = self.deleteNode(root.right, nxt.val)
#         return root
#         
