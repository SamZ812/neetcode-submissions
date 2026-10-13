class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = defaultdict(list)

        for i in strs:
            counts[str(sorted(i))].append(i)

        return list(counts.values())