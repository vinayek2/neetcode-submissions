class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #numbers is non decreasing order 
        for i in range(0, len(numbers)-1, 1):
            for j in range(i+1,len(numbers)):
                if(numbers[i] + numbers[j] != target):
                    continue 
                else:
                    i += 1
                    j += 1
                    return [i, j]