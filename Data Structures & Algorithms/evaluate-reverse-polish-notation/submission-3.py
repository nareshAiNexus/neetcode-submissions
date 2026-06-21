class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbols = ["+", "-", "*", "/"]
        stack = []

        for token in tokens:
            if token not in symbols:
                stack.append(int(token))
            else:
                y = stack.pop()
                x = stack.pop()
            

                if token == "*":
                    aux = x * y

                elif token == "-":
                    aux = x - y

                elif token == "+":
                    aux = x + y

                else:
                    aux = int(x / y)

                stack.append(aux)


        return stack.pop()

                