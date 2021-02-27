class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # dynamic programming
        # create dp array of length equal to amount
        dp = [0] + [999] * amount # the zero is necessary here

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:   # Is current coin less than amount?
                    dp[i] = min(dp[i], dp[i-coin] +1)

        # -1 index means last element in array
        if dp[-1] == 999:
            return -1
        else:
            return dp[-1]
        