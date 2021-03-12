class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = [0]
        
        # prices =  [7,1,5,3,6,4]
        # dp = [0, 0, 4, 4, 7, 7]

        for i in range(1,len(prices)):
            
            if prices[i] > prices[i-1]:
                dp.append(dp[i-1] + prices[i] - prices[i-1])
            else:
                dp.append(dp[i-1])
                
                
        return max(dp)
                


        
        