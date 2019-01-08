#https://leetcode.com/problems/largest-rectangle-in-histogram/description/

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        #copy from answer
        # when cur val < histroy value in stack triger:  so add 0 to triger calculation when last height still > then histroy value.
        #         calculate max
        
        s = []
        ans = 0
        heights.append(0)

        for i in range(len(heights)):
            left_index = i
            while len(s) > 0 and s[-1][0] >= heights[i]:
                last = s.pop()
                left_index = last[1]
                ans = max(ans, heights[i] * (i + 1 - last[1]))
                ans = max(ans, last[0] * (i - last[1]))
            s.append((heights[i], left_index))

        return ans
        
#  give up       
#         if not heights:
#             return 0 
#         max_=-float("inf")
#         s=[]
#         val=0
#         len_=1
#         while heights:
#             cur=heights.pop()
#             while s and s[-1] >=cur:
#                 len_+=1
#                 s.pop()
            
#             if s and s[-1]<cur:
#                 len_=1
#                 s.pop()
            
#             val=len_*cur
#             if val>max_:
#                 max_=val
#             s.append(cur)
            
#         return max_
            
        
        
