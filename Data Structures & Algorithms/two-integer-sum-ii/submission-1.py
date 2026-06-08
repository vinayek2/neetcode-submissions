from collections import defaultdict 
class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        


        '''

        index1 < index2
        
        hashmap 

        {}
        
        
        '''

        for i in range(len(numbers)):
            findNumber = target - numbers[i]
            
            if findNumber in numbers:
                return [i+1, numbers.index(findNumber)+1]
            
            ## numbers[0] is not found then you need to put in map 
                
            
            
            