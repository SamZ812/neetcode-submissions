class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        reference = {"+", "-", "*", "/"}

        for i in range(len(tokens)):
            if tokens[i] in reference:
                op2 = stack.pop()
                op1 = stack.pop()
                if tokens[i] == "+":
                    stack.append(op1 + op2)
                elif tokens[i] == "*":
                    stack.append(op1 * op2)
                elif tokens[i] == "/":
                    stack.append(int(op1 / op2))
                elif tokens[i] == "-":
                    stack.append(op1 - op2)
            else:
                stack.append(int(tokens[i]))
        return stack.pop()