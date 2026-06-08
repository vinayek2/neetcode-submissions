from collections import deque 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        list_deque = deque()
        for element in nums: 
            
            list_deque.append(element)
           
        
        for i in range(len(nums)):
            value = list_deque.popleft()
            current_product = 1
            for j in range(len(list_deque)):
                print(current_product)
                current_product *= list_deque[j]
            output.append(current_product)
            list_deque.append(value)
        
        return output
            
            
            