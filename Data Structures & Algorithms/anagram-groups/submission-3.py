from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublist = {}

        for s in strs:
            sorted_s = "".join(sorted(s))
            
            if sorted_s not in sublist: 
                sublist[sorted_s] = []
            sublist[sorted_s].append(s)
        return list(sublist.values())
        
        
        # res = []
        # sublist = [] 
        # visited = [] 
        # for i in range(0, len(strs), 1):
        #     if(i not in visited):
        #         sublist.append(strs[i])
        #         visited.append(i)
        #     for j in range(i+1, len(strs), 1):
        #         if((Counter(strs[j]) == Counter(strs[i])) and (j not in visited)):
        #             sublist.append(strs[j])
        #             visited.append(j)
        #     if(sublist != []):
        #         res.append(sublist)
        #     sublist = [] 
                    
        
                

        # return res 
                
                
                
            
        