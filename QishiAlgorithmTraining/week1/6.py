#https://leetcode.com/problems/4sum/description/
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        if len(nums)<4:
            return []
        
        
        nums.sort()
        
        result=[]
        
        n=len(nums)
        
        
#         for(int i=0; i<num.length-3; i++){
#         if(num[i]+num[i+1]+num[i+2]+num[i+3]>target)break; //first candidate too large, search finished
#         if(num[i]+num[num.length-1]+num[num.length-2]+num[num.length-3]<target)continue; //first candidate too small
#         if(i>0&&num[i]==num[i-1])continue; //prevents duplicate result in ans list
#         for(int j=i+1; j<num.length-2; j++){
#             if(num[i]+num[j]+num[j+1]+num[j+2]>target)break; //second candidate too large
#             if(num[i]+num[j]+num[num.length-1]+num[num.length-2]<target)continue; //second candidate too small
#             if(j>i+1&&num[j]==num[j-1])continue; //prevents duplicate results in ans list
#             int low=j+1, high=num.length-1;
#             while(low<high){
#                 int sum=num[i]+num[j]+num[low]+num[high];
#                 if(sum==target){
#                     ans.add(Arrays.asList(num[i], num[j], num[low], num[high]));
#                     while(low<high&&num[low]==num[low+1])low++; //skipping over duplicate on low
#                     while(low<high&&num[high]==num[high-1])high--; //skipping over duplicate on high
#                     low++; 
#                     high--;
#                 }
#                 //move window
#                 else if(sum<target)low++; 
#                 else high--;
#             }
#         }

        for i in range(n-3):
            if(nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target): #first val too large
                break
            if (nums[i]+nums[n-1]+nums[n-2]+nums[n-3]<target): #first val too small
                continue
            if(i>0 and nums[i]==nums[i-1]): # when i==i-1 the val already check before
                continue
            for j in range(i+1,n-2):
                if (nums[i]+nums[j]+nums[j+1]+nums[j+2]>target):
                    break  # nums[j] too large
                if (nums[i]+nums[j]+nums[n-1]+nums[n-2]<target):
                    continue  #nums[j] too small
                if (j>i+1 and nums[j]==nums[j-1]):
                    continue #avoid duplication
                
                lo=j+1;hi=n-1
                
                while lo<hi:
                    sum=nums[i]+nums[j]+nums[lo]+nums[hi]
                    if sum==target:
                        result.append([nums[i],nums[j],nums[lo],nums[hi]])
                        while lo<hi and nums[lo]==nums[lo+1]:
                            lo+=1
                        while lo<hi and nums[hi]==nums[hi-1]:
                            hi-=1
                        
                        lo+=1
                        hi-=1
                    elif sum<target:
                        lo+=1
                    else:
                        hi-=1
            
        
 
        return result
                     
                
        
                   
