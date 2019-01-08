#https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        
        """
        
        #BFS with level as key
        
        
        if not root:
            return []
        
        
        q=[]
        
        result=dict()
        
        q.append(root)
        
        level=0
        while q:
            l=len(q)
            result[level]=[]
            for i in range(l):
                node=q.pop(0)
                result[level].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
            
            
        r=[]
        for k,v in result.items():
            if k%2==1:
                v=v[::-1]
            r.append(v)
        return r
    
    
                
            
            
        
