import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        '''
        dictionary->map 
        map key, value
        key = index: 
        '''
        mapper = {}
        temp = nums.copy()
        # print(f"temp: {temp}")

        for i in range(len(nums)):
            mapper[i] = (temp[i+1:len(temp)])
            mapper[i]+= (temp[0:i])
        # print(f"Mapper: {mapper}")
        res = []
        for i in range(len(mapper)):
             

            res.append(math.prod(mapper[i]))
            
            # print(f"res: {res}")

        return res 