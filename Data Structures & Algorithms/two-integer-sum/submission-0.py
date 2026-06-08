class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track_values = dict()
        for i in range(len(nums)):
            
            complement = target - nums[i]

            if complement in track_values:
                return [track_values[complement], i]
            
            track_values[nums[i]] = i
        
        