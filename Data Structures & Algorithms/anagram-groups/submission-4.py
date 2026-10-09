class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []

        words = defaultdict(list)

        for i in strs:
            words[str(sorted(i))].append(i)
        
        return list(words.values())
            