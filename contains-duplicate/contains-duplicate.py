class Solution(object):
    def containsDuplicate(self, nums):
        myDict = {"numbers": []}
        
        for num in nums:
            if num in myDict["numbers"]:
                return True
            myDict["numbers"].append(num)
            
        return False
            