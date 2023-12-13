class Solution:
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(l,r,nums):
            while l < r:
                nums[r],nums[l] = nums[l],nums[r]
                l,r = l+1,r-1
        k = k % len(nums) 
        reverse(0,len(nums) - 1,nums)
        reverse(0,k-1,nums)
        reverse(k,len(nums) - 1,nums)
        
        
        
        
        
        
            