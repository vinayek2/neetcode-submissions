class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in range(len(strs)):
            s += strs[i]+ "~"
        
        return s 
    
            

            

    def decode(self, s: str) -> List[str]:
        res = s.split("~")
        return res[:-1]
