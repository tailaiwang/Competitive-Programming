#Sum or Root to Leaf Binary Numbers
#https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
#Easy (Daily Challenge), 11/01/2022
#Tailai Wang

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        paths = []
        def helper (root, path):
            path = path + str(root.val)
            if (root.left == None and root.right == None):
                paths.append(path)
                return
            if (root.left != None):
                helper(root.left, path)
            if (root.right != None):
                helper(root.right, path)
        helper(root, "")
        total = 0
        for path in paths:
            for i in range(len(path)):
                if (path[i] == "1"):
                    total += 2 ** (len(path) - 1 - i)
        return(total)
