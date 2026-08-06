class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                tot = stack.pop() + stack.pop()
                stack.append(tot)
            elif token == "-":
                minus = stack.pop()
                tot = stack.pop() - minus
                stack.append(tot)
            elif token == "/":
                div = stack.pop()            
                tot = int(stack.pop()  / div)  
                stack.append(tot)
            elif token == "*":
                tot = stack.pop() * stack.pop()
                stack.append(tot)
            else:
                stack.append(int(token))
        return stack[0]


