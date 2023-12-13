class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current = 0
        count = 0
        for i in range(len(nums)):
            if count <= 0:
                current = nums[i]
                count = 1
            else:
                if current == nums[i]:
                    count += 1
                else:
                    count -= 1
        return current