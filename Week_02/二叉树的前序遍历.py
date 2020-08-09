#
# @lc app=leetcode.cn id=144 lang=python
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
        
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ens = []
        if root == None:
            return ens
        self.preTraverse(root, ens)
        return ens
    def preTraverse(self,t, ens):
        ens.append(t.val)
        if t.left:
            self.preTraverse(t.left, ens)
        if t.right:
            self.preTraverse(t.right, ens)

            
# @lc code=end

