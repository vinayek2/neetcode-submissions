class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Input: nums = [2,20,4,10,3,4,5]

        Output: 4

        visited 

        mps = {}
        key: 2 
        2 -> 20
        2 -> 4 -> 10 
        2 -> 3 -> 4 -> 5

        visited

        
        '''

        numset = set(nums)
        
        longest = 0 

        for num in numset:
            if num-1 not in numset:
                numset.add(num)
                length = 1
                while(num+length in numset):
                    length +=1 
                longest = max(longest, length)
        return longest 

        
        
                
        
        
                
            
        
        
        
                
                
                
            
            