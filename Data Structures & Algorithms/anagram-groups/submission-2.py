class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        result = []
        for strings in strs:
            sortedString = ''.join(sorted(strings))
            anagrams[sortedString].append(strings)
        return list(anagrams.values())