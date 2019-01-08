#https://leetcode.com/problems/first-missing-positive/description/
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Input: [7,8,9,11,12]
        Output: 1
        """
        
        lennums=len(nums)
        
        if lennums==0:
            return 1
    
        numset=set()
        for num in nums:
            if num>0:
                numset.add(num)
                
        for i in range(1,lennums+2):
            if i not in numset:
                return i
          
        
        
   
        
                
        
        
        
    
            
        
        
