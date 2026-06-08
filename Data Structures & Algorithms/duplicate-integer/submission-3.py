class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print(f"New List: {list(set(nums))}")
        print(f"Old List: {nums}")
        
        return not (len(list(set(nums))) == len(nums))
        
        