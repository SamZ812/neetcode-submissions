class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in strs:
            sortedString = ''.join(sorted(i))
            hashmap[sortedString].append(i)
            
        return list(hashmap.values())