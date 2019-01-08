#https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q=[]
        q.append(root)
        result=[]
        while q:
            l=len(q)
            level=[]
            for i in range(l):
                top=q.pop(0)
                level.append(top.val)
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
            result.append(level)
            
        return result[::-1]
                    
                
