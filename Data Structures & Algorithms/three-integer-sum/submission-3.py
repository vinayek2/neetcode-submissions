from collections import Counter 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # visited = dict()
        # track_zeros = []
        # for i in range(0, len(nums)):
        #     for j in range(1, len(nums)-1):
        #         if((nums[i] in visited) | (nums[j] in visited)):
        #             continue 
        #         totalSum = nums[i] + nums[j]
        #         target = -(totalSum)
        #         if target in nums: 
        #             track_zeros.append([nums[i], nums[j], target])
        #         visited[nums[i]] = i 
        #         visited[nums[j]] = j 
        # return track_zeros

        track_zeros=[]
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:#prevent same value twice and idx is not first entry 
                continue
            l, r = i+1, len(nums)-1
            while(l < r):
                threeSum = nums[l] + nums[r] + a
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    track_zeros.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r :
                        l+=1 
        return track_zeros
                    
                
                
                    
        
        


            
        