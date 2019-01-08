https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Input:
         0 1 2 3 4 5 6 7
        [4,3,2,7,8,2,3,1]
        add 4  into pos 3        
           [7] = 7%8 
           pos3val now     = 4*8+[7]
           pos3val original=(4*8+[7])%8 
        Output:
        [5,6]
        
        
        [10,2,5,10,9,1,1,4,3,7]
        [1,6,8]
        """
        result=[]
        lennums=len(nums)
        for num in nums:
            pos=num%lennums-1
            nums[pos] += num*lennums
        
        for pos in range(lennums):
            if nums[pos]<=lennums:
                result.append(pos+1)
            
        return result
        
        
        
        
        
        
        
        
