
class Solution:

    def isNumber(self, s) -> bool:
        try:
            int(s)
            return True; 
        except ValueError: 
            return False
    def evalRPN(self, tokens: List[str]) -> int:
        '''

        "1" , "2" , "3", "
        
        '''
        stack = [] 
        index = 0 

        output = 0 

        while(index != len(tokens)):
            if(self.isNumber(tokens[index])):
                stack.append(tokens[index])
            else:
                if(tokens[index] == "+"):
                    if(len(stack)>1):
                        add1 = stack.pop()
                        add2 = stack.pop()
                        output = int(add1) + int(add2)
                        stack.append(output)
                elif(tokens[index] == "-"):
                    if(len(stack)>1):
                        sub1 = stack.pop()
                        sub2 = stack.pop()
                        output = int(sub2) - int(sub1)
                        stack.append(output)
                    
                elif(tokens[index] == "*"):
                    if(len(stack)>1):
                        m1 = stack.pop()
                        m2 = stack.pop()
                        output = int(m1) * int(m2)
                        stack.append(output)
                elif(tokens[index] == "/"):
                    if(len(stack)>1):
                        bottom = stack.pop()
                        top = stack.pop()
                        output = int(top)/int(bottom)
                        stack.append(output)
            index+=1 
                     
            
        return int(stack[-1])
            
            

    
            
        
        


        
        