class Solution:
    def maxArea(self, height: List[int]) -> int:
       
        left = height[0]
        right = height[-1]
        # think of case where input is [1,1]
        
        rightIdx = len(height) -1
        leftIdx = 0
        
        maxAr = 0
    
        while rightIdx > leftIdx:
            
            maxAr = max(maxAr, min(left,right) * (rightIdx - leftIdx))
            
            # figure out which way to go, either left += 1 or right -=1
            # if right is bigger, do left += 1
            
            if right > left:
                leftIdx +=1
                left = height[leftIdx]
            else:
                rightIdx -= 1
                right = height[rightIdx]
                
        return maxAr
            