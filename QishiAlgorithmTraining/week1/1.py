#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        [7,1,5,3,6,4,7]
        """
        minval=999999
        maxdiff=0
        for price in prices:
            if price<minval:
                minval=price
            diff=price-minval
            if diff>maxdiff:
                maxdiff=diff
        return maxdiff
        
