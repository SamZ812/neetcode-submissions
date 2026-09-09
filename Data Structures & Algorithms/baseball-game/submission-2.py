class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        record = []
        
        for i in operations:
            if i == "+":
                val = record[-1] + record[-2]
                record.append(val)
                stack.append(val)
            elif i == "C":
                stack.pop()
                record.pop()
            elif i == "D":
                stack.append(stack[-1] * 2)
                record.append(record[-1] * 2)
            else:
                stack.append(int(i))
                record.append(int(i))

        return sum(record)


                