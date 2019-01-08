#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        Input: [3,3,5,0,0,3,1,4]
        dr      0 2-5 0 3-2 3
        Output: 6
              [1,2,3,4,5]
        dr     1 1 1 1
        Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
        
        dp[k, i] = max(dp[k, i-1], prices[i] - prices[j] + dp[k-1, j-1]), j=[0..i-1]
        
        kth transanction on ith day.
        
          if (prices.Length == 0) return 0;
            var dp = new int[3, prices.Length];
            for (int k = 1; k <= 2; k++)  {
                for (int i = 1; i < prices.Length; i++) {
                    int min = prices[0];
                    for (int j = 1; j <= i; j++)
                        min = Math.Min(min, prices[j] - dp[k-1, j-1]);
                    dp[k, i] = Math.Max(dp[k, i-1], prices[i] - min);
                }
            }

            return dp[2, prices.Length - 1];
            
            
            
            
            
            
            for (int k = 1; k <= 2; k++) {
                int min = prices[0];
                for (int i = 1; i < prices.Length; i++) {
                    min = Math.Min(min, prices[i] - dp[k-1, i-1]);
                    dp[k, i] = Math.Max(dp[k, i-1], prices[i] - min);
                }
            }
            
            
            
            
            
            
         if (prices.Length == 0) return 0;
            var dp = new int[3, prices.Length];
            var min = new int[3];
            Array.Fill(min, prices[0]);
            for (int i = 1; i < prices.Length; i++) {
                for (int k = 1; k <= 2; k++) {
                    min[k] = Math.Min(min[k], prices[i] - dp[k-1, i-1]);
                    dp[k, i] = Math.Max(dp[k, i-1], prices[i] - min[k]);
                }
            }
        
        """
#         if len(prices)==0:
#             return 0
        
#         dp=[ [0 for __ in range(len(prices))] for _ in range(3)]
        
        
#         for k in range(1,3):
#             min_=prices[0]
#             for i in range(1,len(prices)):
#                 min_=min([min_,prices[i]-dp[k-1][i-1]])
#                 pricei_min=prices[i]-min_
#                 dp[k][i]=max([dp[k][i-1],pricei_min])
           
#         return dp[2][len(prices)-1]

#-------------------
        
#         if len(prices)==0:
#             return 0
#         dp=[ [0 for __ in range(len(prices))] for _ in range(3)]
#         min_=[prices[0] for _ in range(3)]
        
#         for i in range(1,len(prices)):
#             for k in range(1,3):
#                 min_[k]=min([min_[k],prices[i]-dp[k-1][i-1]])
#                 dp[k][i]=max([dp[k][i-1],prices[i]-min_[k]])
        
        
        
#         return dp[2][len(prices)-1]

#-----------
#        if (prices.Length == 0) return 0;
#             var dp = new int[3];
#             var min = new int[3];
#             Array.Fill(min, prices[0]);
#             for (int i = 1; i < prices.Length; i++)  {
#                 for (int k = 1; k <= 2; k++) {
#                     min[k] = Math.Min(min[k], prices[i] - dp[k-1]);
#                     dp[k] = Math.Max(dp[k], prices[i] - min[k]);
#                 }
#             }

#             return dp[2];
        if len(prices)==0:
            return 0
        dp=[0,0,0]
        min_=[prices[0],prices[0],prices[0]]
        for i in range(1,len(prices)):
            for k in range(1,3):
                min_[k]=min([min_[k],prices[i]-dp[k-1]])
                dp[k]=max(dp[k],prices[i]-min_[k])
        

        return dp[2]
