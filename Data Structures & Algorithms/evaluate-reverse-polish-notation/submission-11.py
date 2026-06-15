class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = ["+", "-", "/", "*"]
        
        for t in tokens:
            if t in symbols:
                # The first pop is the second operand
                right = stack.pop()
                # The second pop is the first operand
                left = stack.pop()
                
                if t == "+":
                    stack.append(left + right)
                elif t == "-":
                    stack.append(left - right)
                elif t == "*":
                    stack.append(left * right)
                elif t == "/":
                    # Truncate toward zero logic
                    stack.append(int(left / right))
            else:
                # It's a number, convert and push
                stack.append(int(t))
                
        return stack[0]