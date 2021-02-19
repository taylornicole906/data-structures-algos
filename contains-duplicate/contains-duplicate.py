class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # use set
        setList = list(set(nums))
        if len(setList) != len(nums):
            return True
        else:
            return False