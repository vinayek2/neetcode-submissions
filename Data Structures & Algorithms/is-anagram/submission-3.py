from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        for i in range(len(s)):
            map1[s[i]] = 0
        print(map1)
        for j in range(len(t)):
            map2[t[j]] = 0
        print(map2)



        for i in range(len(s)):
            map1[s[i]] += 1
        print(map1)
        for j in range(len(t)):
            map2[t[j]] += 1
        print(map2)
        return (map1 == map2)