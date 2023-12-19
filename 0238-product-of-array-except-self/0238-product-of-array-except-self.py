class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]
        j = len(nums) - 2
        add = 1
        
        for i in range(1,len(nums)):
            output.append(nums[i-1] * output[i-1])
        
        while j >= 0:
            add *= nums[j+1]
            output[j] = add * output[j]
            j -= 1
            
        return output
            