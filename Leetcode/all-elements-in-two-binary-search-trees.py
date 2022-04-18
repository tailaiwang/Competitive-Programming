#All Elements in Two Binary Search Trees
#https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
#Medium (Daily Challenge), 26/01/2022
#Tailai Wang

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        elements =[]
        def traverse(root):
            if (root != None):
                elements.append(root.val)
                if (root.left != None):
                    traverse(root.left)
                if (root.right != None):
                    traverse(root.right)
        traverse(root1)
        traverse(root2)
        elements.sort()
        return elements
