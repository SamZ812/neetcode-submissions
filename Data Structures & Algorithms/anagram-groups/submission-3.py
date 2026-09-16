class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = defaultdict(list)

        for i in strs:
            sortedStr = str(''.join(sorted(list(i))))
            counts[sortedStr].append(i)

        return list(counts.values())