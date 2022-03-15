<<<<<<< HEAD
#Insert into a Binary Search Tree
#https://leetcode.com/problems/insert-into-a-binary-search-tree/
#Medium (Daily Challenge), 12/01/2022
#Tailai Wang

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def helper(node, value):
            if (value < node.val):
                if (node.left != None):
                    helper(node.left, value)
                else:
                    node.left = TreeNode(value)
                    return
            else:
                if (node.right != None):
                    helper(node.right, value)
                else:
                    node.right = TreeNode(value)
                    return
        if (root == None):
            return TreeNode(val)
        else:
            helper(root, val)
            return root
=======
#Insert into a Binary Search Tree
#https://leetcode.com/problems/insert-into-a-binary-search-tree/
#Medium (Daily Challenge), 12/01/2022
#Tailai Wang

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def helper(node, value):
            if (value < node.val):
                if (node.left != None):
                    helper(node.left, value)
                else:
                    node.left = TreeNode(value)
                    return
            else:
                if (node.right != None):
                    helper(node.right, value)
                else:
                    node.right = TreeNode(value)
                    return
        if (root == None):
            return TreeNode(val)
        else:
            helper(root, val)
            return root
>>>>>>> ba49908b5b4d7d2990ceb0c0f59ad013ea443c99
