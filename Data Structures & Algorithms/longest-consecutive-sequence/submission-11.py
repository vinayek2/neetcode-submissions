
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ## Perhaps use suffix and prefix terminology 
        if(len(nums) == 0):
            return 0
        quicklist = set(nums)
       
        track_max = []

        for i in quicklist:
            if i-1 not in quicklist:
                tracker = 1 
                while i+1 in quicklist: 
                    tracker += 1
                    i = i+1
                track_max.append(tracker)
            
        return max(track_max)
        