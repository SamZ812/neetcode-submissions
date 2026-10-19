class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "/", "*", "-"}

        stack = []

        for i in tokens:
            if i in operators:
                operator2 = stack.pop()
                operator1 = stack.pop()
                if i == "+":
                    stack.append(operator1 + operator2)
                elif i == "-":
                    stack.append(operator1 - operator2)
                elif i == "*":
                    stack.append(operator1 * operator2)
                elif i == "/":
                    stack.append(int(operator1 / operator2))
            else:
                stack.append(int(i))

        return stack.pop()