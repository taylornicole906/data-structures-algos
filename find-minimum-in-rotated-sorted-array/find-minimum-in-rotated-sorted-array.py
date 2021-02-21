class Solution:
    def findMin(self, nums: List[int]) -> int:
         #binary search
        left, right = 0, len(nums) - 1
        
        while nums[left] > nums[right]:
            center  = (left + right) // 2
            
            if nums[center] < nums[right]:
                right = center
            else:
                left = center + 1
        return nums[left]
        
        