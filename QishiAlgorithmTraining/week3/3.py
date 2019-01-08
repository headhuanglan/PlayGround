#https://leetcode.com/problems/next-greater-element-ii/description/

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Input: [1,2,1]
        Output: [2,-1,2]
        """
        
        # #excess time limit
        # l=len(nums)
        # result=[-1]*len(nums)
        # for i in range(l):
        #     for j in range(1,l):
        #         if nums[(i+j) % l] > nums[i]:
        #             result[i]=nums[(i+j) % l]
        #             break
        # return result
        
#Copy solution         need read the analysis if have time
#         public int[] nextGreaterElements(int[] nums) {
#         int[] res = new int[nums.length];
#         Stack<Integer> stack = new Stack<>();
#         for (int i = 2 * nums.length - 1; i >= 0; --i) {
#             while (!stack.empty() && nums[stack.peek()] <= nums[i % nums.length]) {
#                 stack.pop();
#             }
#             res[i % nums.length] = stack.empty() ? -1 : nums[stack.peek()];
#             stack.push(i % nums.length);
#         }
#         return res;
 
#     index  0 1 2
#            1 2 3
        l=len(nums)    
        result=[0]*l
        s=[]
        for i in range(2*len(nums)-1,-1,-1):
            while s and nums[s[-1]]<=nums[i % l]:
                s.pop()
            if s:
                result[i % l]= nums[s[-1]]
            else:
                result[i % l]=-1
            s.append(i%l)
        return result
        
        
        
 
        
