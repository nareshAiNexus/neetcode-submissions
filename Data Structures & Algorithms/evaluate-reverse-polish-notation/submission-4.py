class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        symbols = set("+-/*")
        stack = []

        for token in tokens:
            if token not in symbols:
                stack.append(token)
            else:
                x, y = stack.pop(), stack.pop()
                stack.append(str(int(eval(y + token + x))))
        return int(stack[0])