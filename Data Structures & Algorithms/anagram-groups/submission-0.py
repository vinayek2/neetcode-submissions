from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if(len(strs) == 0):
            return strs 
        if(len(strs) == 1):
            return [strs]
        main_list = []
        visited = {s: False for s in strs}
        for i in range(0, len(strs)):
            if(visited[strs[i]] == False):
                sublist = []
                sublist.append(strs[i])
                for j in range(i+1, len(strs)):
                    if(Counter(strs[i]) == Counter(strs[j])):
                        sublist.append(strs[j])
                        # strs.remove(strs[j])
                        visited[strs[j]] = True
                main_list.append(sublist)
                visited[strs[i]] = True
        return main_list
                
            