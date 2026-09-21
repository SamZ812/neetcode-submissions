class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            delimiter = s.find("#", i)
            length = int(s[i:delimiter])
            result.append(s[delimiter + 1 : delimiter + 1 + length])
            i = delimiter + 1 + length
        return result