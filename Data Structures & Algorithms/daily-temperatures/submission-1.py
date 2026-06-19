class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        count = 0 
        result = []
        k = 0 
        i = 0 
        
        while(k < len(temperatures)):
            found = False 
            j = i + 1 
            while(j < len(temperatures)):
                if(temperatures[i] < temperatures[j]):
                    found = True
                    count = j - i 
                    break 
                j += 1
            if(found == False):
                count = 0
            result.append(count)
            count = 0 
            i += 1 
            k += 1 
        return result 
                 