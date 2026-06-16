class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else: 
                counts[num] = 1

        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])

        for num in counts:
            buckets[counts[num]].append(num)
        
        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result
        