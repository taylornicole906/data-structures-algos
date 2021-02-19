class Solution(object):
    def lengthOfLIS(self, nums):
        # dynamic programming
        
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j] and dp[i]<dp[j]+1:
                    dp[i] = dp[j] + 1
                    
        return max(dp)


       
    
            
       
    
        