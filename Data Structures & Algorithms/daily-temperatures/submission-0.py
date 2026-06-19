class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        count = 0 
        result = []
        k = 0 
        i = 0 
        
        while(k < len(temperatures)):
            j = i + 1
            found = False
            while(j < len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    count = j - i
                    found = True
                    break
                j+=1 
            if not found:
                count = 0
            result.append(count)
            count = 0
            k+=1 
            i += 1
        return result