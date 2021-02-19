class Solution(object):
    def climbStairs(self, n):
        
        if n == 1:
            return 1
        
        dp = [1, 2, 3]  
        for i in range(3, n):
            elem = dp[i -1] + dp[i -2]
            dp.append(elem)
            
        return dp[n-1]