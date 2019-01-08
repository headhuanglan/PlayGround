#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        [7,1,5,3,6,4]
        -6 4-2 3-2 
        """
        dailyreturn=[0]*(len(prices)-1)
        for i in range(1,len(prices)):
            dailyreturn[i-1]=prices[i]-prices[i-1]
         
        profit=0
        for r in dailyreturn :
            if r>0:
                profit+=r
    
                
        return profit
            
        
        
