class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        
        for i in operations:
            if i == "+":
                val = record[-1] + record[-2]
                record.append(val)
            elif i == "C":
                record.pop()
            elif i == "D":
                record.append(record[-1] * 2)
            else:
                record.append(int(i))

        return sum(record)


                