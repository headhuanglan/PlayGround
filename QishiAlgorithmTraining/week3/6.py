#https://leetcode.com/problems/binary-tree-preorder-traversal/description/

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
        
        done=False
        s=[]
        result=[]
        cur=root
        
        while not done:
            if cur:
                result.append(cur.val)
                s.append(cur)
                cur=cur.left
            else:
                if s:
                    cur=s.pop()
                    cur=cur.right
                else:
                    done=True
        return result
        

        
#         trivial solution-----------        
#         result=[]
#         left=None
#         right=None
#         if root==None:
#             return result
        
        
#         if root.left:
#             left=self.preorderTraversal(root.left)
#         if root.right:
#             right=self.preorderTraversal(root.right)
            
        
#         result.append(root.val)
#         if left:
#             result.extend(left)
#         if right:
#             result.extend(right)
            
#         return result
           
            
            
