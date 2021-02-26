class Solution:
    def rob(self, nums: List[int]) -> int:
            if len(nums) == 0:
                return 0
            if len(nums) == 1:
                return nums[0]

            # dp array stores max profit at each house.
            # create first two elements in dp array
            # first question, do we rob 1st house or second house?
            dp = [nums[0], max(nums[0], nums[1])]
            # if we rob 2nd house, next question is do we rob 1st + 3rd, or just second?
            for i in range(2, len(nums)):
                dp.append(max(dp[i - 1], dp[i - 2] + nums[i]))

            return max(dp)
            
            
            
                
        