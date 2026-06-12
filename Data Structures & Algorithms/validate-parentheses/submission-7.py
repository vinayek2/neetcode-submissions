class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        characters = {"}":"{", ")":"(","]":"["}
        
        for c in s: 
            if c in characters: 
                if stack and stack[-1] == characters[c]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(c)

        
            
            
                    
        return True if not stack else False 

        
        
        