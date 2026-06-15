class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublist = {}
        for s in strs:
            sort_s = "".join(sorted(s))
            
            if sort_s not in sublist:
                sublist[sort_s] = []
            
            sublist[sort_s].append(s)
        return list(sublist.values())
                
        