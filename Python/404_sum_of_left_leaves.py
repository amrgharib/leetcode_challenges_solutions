# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode, isleft=False) -> int:
        if root==None:
            return 0
        if root.left==None and root.right==None:
            if isleft:
                return root.val
            else:
                return 0
        return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right, False)


# Top solution with while loop
#class Solution:
#    def sumOfLeftLeaves(self, root: TreeNode) -> int:
#        tot = 0
#        dfs = [root]
#        
#        if not root:
#            return 0
#        
#        def isLeaf(root):
#            return root and not root.left and not root.right
#        
#        while dfs:
#            current = dfs.pop()
#            if not current.left and not current.right and current != root:
#                tot += current.val
#            if current.left:
#                dfs.append(current.left)
#            if current.right and not isLeaf(current.right):
#                dfs.append(current.right)
#        return tot
