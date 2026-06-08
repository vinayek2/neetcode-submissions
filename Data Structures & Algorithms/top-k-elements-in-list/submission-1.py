from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashes = Counter(nums)
        sublist = []
        for i in range(k):
            key = max(hashes, key=hashes.get)
            sublist.append(key)
            hashes.pop(key)
        return sublist
            
            
        
            