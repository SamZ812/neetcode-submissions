class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            result = result + i + "~"
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        string = ""
        for i in s:
            if i == "~":
                result.append(string)
                string = ""
            else:
                string = string + i
        return result
