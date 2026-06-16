class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sums = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            sums[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            sums[i] *= postfix
            postfix *= nums[i]

        return sums
            
        
        