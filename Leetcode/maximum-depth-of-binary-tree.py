#Maximum Depth of Binary Tree
#https://leetcode.com/problems/maximum-depth-of-binary-tree/
#Easy, 03/02/2022
#Tailai Wang

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    retVal = 1
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        
        def helper(root, cur):
            if (root.left == None and root.right == None):
                self.retVal = max(self.retVal, cur)
            else:
                if (root.left != None):
                    helper(root.left, cur + 1)
                if (root.right != None):
                    helper(root.right, cur + 1)
        
        helper(root, 1)
        return self.retVal
