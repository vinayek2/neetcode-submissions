from collections import Counter 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ## Perhaps use suffix and prefix terminology 
        nums = list(set(nums))
        nums = sorted(nums)
        quicklist = Counter(nums)
        tracker = 1

        max_value = 0 
        for i in range(len(nums)-1, -1, -1):
            previous_element = nums[i] - 1
            print(tracker)
            if previous_element in quicklist:
                print(f'{nums[i]-1} in the list')
    
                tracker += 1
                continue

                # hwo do i jump 
                print(tracker)
            else:
                #make that an official list
                
                print(f'{nums[i]-1} not in the list')
                if(max_value < tracker): 
                    
                    max_value = tracker
                tracker = 1
        return max_value 
        