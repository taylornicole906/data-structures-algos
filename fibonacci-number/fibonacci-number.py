class Solution(object):
    def fib(self, n):
        
        dp = [0, 1, 1]
        
        for x in range(3, n + 1):
            # append next number to dp array
            dp.append(dp[x-1] + dp[x-2])
            
        return dp[n]
        
    
    
        