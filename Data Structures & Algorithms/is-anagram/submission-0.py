from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_one = Counter(s)
        list_two = Counter(t)

        return list_one == list_two
        
        
        