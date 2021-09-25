class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            x = target - nums[i]
            for j in range(1, len(nums)):
                if nums[j] == x and i != j:
                    return [i,j]
            
                
        