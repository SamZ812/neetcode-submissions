class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"{":"}", "[":"]", "(":")"}
        stack = []

        if len(s) % 2 != 0:
            return False

        for char in s:
            if char in hashmap:
                stack.append(char)
            else:
                if stack and hashmap[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True