from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapper = Counter(nums)
        freq = [[] for i in range(len(nums)+1)] #len(nums) + 1
        result = []
        count = 0

        for key, val in mapper.items():
            freq[val].append(key)
        
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result)==k:
                    return result 

     


                