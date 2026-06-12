class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lister = set() 
        nums = sorted(nums)
        
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1 
            while(l<r):
                curr = nums[i] + nums[l] + nums[r]
                if(curr > 0):
                    r -= 1

                elif(curr < 0):
                    l += 1 
                else: 
                    element = [nums[l],nums[r], nums[i]]
                    lister.add(tuple(sorted(element)))
                    l+=1 

     
        return list(lister)

                
                

                    
                    