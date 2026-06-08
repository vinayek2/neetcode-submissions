class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        stack = [("", 0, 0)]
        while(len(stack) != 0): 
            prefix, open_used, closed_used = stack.pop()

            if(len(prefix) == 2*n):
                output.append(prefix)
                continue #found a valid string 

            if(open_used < n):
                stack.append((prefix+"(", open_used+1, closed_used))
                
            if(closed_used < open_used):
                stack.append((prefix+")", open_used, closed_used+1))
        

        return output 
            
            
        
            
            
            
                
                
            
            
            
            
            
        
        
            
        
        
            
                
            
    