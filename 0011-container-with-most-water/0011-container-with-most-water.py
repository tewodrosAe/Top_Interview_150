class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxCont = 0
        
        while l < r:
            distance =  r - l
            maxCont = max(maxCont, min(height[l],height[r]) * distance)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
            
        
        return maxCont