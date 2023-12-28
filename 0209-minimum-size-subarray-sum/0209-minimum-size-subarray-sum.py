class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        l,r,total = 0, 0, 0
        minDist = len(nums) 
        while r < len(nums): 
            total += nums[r]
            while total >= target:
                minDist = min(minDist, r - l + 1)
                total -= nums[l]
                l += 1
            r += 1
                
        return minDist