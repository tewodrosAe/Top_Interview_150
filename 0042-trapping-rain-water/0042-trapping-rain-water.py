class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height: return 0
        total = 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        
        while l < r:
            if maxL > maxR:
                r -= 1
                maxR = max(maxR, height[r])
                total += maxR - height[r]
            else:
                l += 1
                maxL = max(maxL, height[l])
                total += maxL - height[l]
        return total
            
        