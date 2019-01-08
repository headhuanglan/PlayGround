#https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
 
        """
        #pre order right->left then result[::-1]
        
        done=False
        s=[]
        result=[]
        cur=root
        
        while not done:
            if cur:
                result.append(cur.val)
                s.append(cur)
                cur=cur.right
            else:
                if s:
                    cur=s.pop()
                    cur=cur.left
                else:
                    done=True
        return result[::-1]
                    
        
                
        
# trivial solution        
#
#         if not root:
#             return []
        
#         result=[]
#         left=None
#         right=None
        
#         if root.left:
#             left=self.postorderTraversal(root.left)
#         if root.right:
#             right=self.postorderTraversal(root.right)
            
        
#         if left:
#             result.extend(left)
#         if right:
#             result.extend(right)
#         result.append(root.val)
        
        
#         return result
            
        
